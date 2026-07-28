#!/usr/bin/env python3
"""Grep a document's markdown and code comments for the mechanical voice tells.

Usage: python prose_lint.py <notebook.ipynb> [...]

Catches the recurring, greppable violations from notebook-authoring.md. It cannot
judge openers or altitude — the written opener audit still runs by hand — but it
catches the patterns that keep leaking back. Zero exit = no hits.
"""
import json
import re
import sys

RULES = [
    # (name, regex, applies_to)  applies_to: md, comment, or both
    ("animate-verb", re.compile(
        r"\b(live[s]? (in|as|on)|rides? along|sits? (in|on|at)|carries|carry\b|owns\b|journey|"
        r"lands? (as|in|on)|comes? home|breathes?|wants? to)\b", re.I), "both"),
    ("banned-term", re.compile(
        r"\b(corpus|smoke test|smoke run|de-facto|payoff|skeeze|full stop)\b", re.I), "md"),
    ("fm-abbrev", re.compile(r"(?<![`/\w])fm(?![`\w])"), "md"),
    ("movie-preview", re.compile(
        r"\b(the one (line|knob|thing)|that's (all|it) it takes|is all it takes|"
        r"the magic|the beauty of|the payoff is)\b", re.I), "both"),
    ("announce-label", re.compile(
        r"^#*\s*(The |A |One |Two |Three |Four |Note:|Important:|Key )\w[\w '\-]{0,30}:\s", ), "comment"),
    ("negative-opener", re.compile(
        r"^(No |Nothing |Never |Not |Neither |Nobody )"), "both"),
    ("because-tail", re.compile(
        r", because [^.]{10,}\.\s*$"), "md"),
    ("notation-as-prose", re.compile(
        r"`[^`]+`\s*\+\s*`[^`]+`"), "md"),
    ("label-bullet", re.compile(
        r"^\s*[-*]\s+\*\*[\w /()]+\*\*\s*:"), "md"),
    ("dash-inventory", re.compile(
        r"—[^—.\n]*`[^`]+`\s*,\s*`[^`]+`[^.\n]*\.\s*$"), "md"),
    ("dash-aside-sandwich", re.compile(
        r"—[^.—\n]{5,90}—[^.\n]{0,60}\bso\b"), "md"),
    ("announced-contrast", re.compile(
        r"\b(with one (big )?difference|but here's the (catch|twist)|the catch is)\b", re.I), "both"),
    ("punctuation-pile", re.compile(
        r"[^.!?]*:[^.!?]*\([^)]*\)[^.!?]*;"), "md"),
    # Earned punctuation (Zach, Jul 2026): every em-dash, colon, and especially
    # semicolon must be earned; multiples in one sentence are a pile. Flag every
    # semicolon and every doubled mark (two em-dashes, or a mark plus another).
    ("semicolon", re.compile(r";"), "md"),
    ("doubled-punctuation", re.compile(r"[—:;][^.!?\n]*[—:;]"), "md"),
    ("grandstand", re.compile(
        r"\b(the artifact every|is what makes .{0,40} possible|this is the moment|"
        r"the heart of|the whole (game|point|story) is)\b", re.I), "md"),
]


def lint_notebook(path):
    hits = []
    nb = json.load(open(path))
    for c in nb.get("cells", []):
        cid = c.get("id", "?")
        src = "".join(c.get("source", []))
        if c.get("cell_type") == "markdown":
            for ln, line in enumerate(src.splitlines(), 1):
                for name, rx, scope in RULES:
                    if scope in ("md", "both") and rx.search(line):
                        hits.append((path, cid, f"md:{ln}", name, line.strip()[:90]))
        elif c.get("cell_type") == "code":
            for ln, line in enumerate(src.splitlines(), 1):
                if "#" not in line:
                    continue
                comment = line[line.index("#"):]
                for name, rx, scope in RULES:
                    if scope in ("comment", "both") and rx.search(comment):
                        hits.append((path, cid, f"code:{ln}", name, comment.strip()[:90]))
    return hits


def audit_imports(nb_path):
    """List every name a notebook imports from src/, with size and Ray content —
    the facts for the show-or-hide call. Usage: prose_lint.py --imports <nb>"""
    import glob
    nb = json.load(open(nb_path))
    imported = []
    for c in nb.get("cells", []):
        if c.get("cell_type") != "code":
            continue
        src = "".join(c.get("source", []))
        for m in re.finditer(r"from (src\.\w+) import \(?([^)\n]+)\)?", src):
            mod = m.group(1).replace(".", "/") + ".py"
            names = [n.strip() for n in m.group(2).split(",") if n.strip()]
            imported.append((mod, names))
    for mod, names in imported:
        try:
            code = open(mod).read()
        except OSError:
            print(f"{mod}: NOT FOUND")
            continue
        for name in names:
            dm = re.search(r"(@ray\.remote[^\n]*\n)?(def |class )" + name +
                           r"\b.*?(?=\n@|\ndef |\nclass |\Z)", code, re.S)
            if not dm:
                print(f"{mod}:{name}  (not a def/class — constant or re-export)")
                continue
            body = dm.group(0)
            rays = sorted(set(re.findall(r"@ray\.remote|ray\.get|\.remote\(|ray\.data\.\w+|"
                                         r"map_batches|map_groups|ray\.train", body)))
            print(f"{mod}:{name}  {body.count(chr(10))} lines  ray={rays or 'NONE'}")


def audit_openers(path):
    """Set up the mandatory written opener audit for an HTML doc. For every
    section, print its heading, its first body sentence, and its last body
    sentence — the reviewer fills in the section's one-line claim and the verdict
    "is sentence one THAT claim?" A section opener that is a label, a definition,
    motivation, or backstory FAILS even with zero mechanical hits. The linter
    can't judge this; producing the table is what makes the review happen.
    Usage: prose_lint.py --openers <file.html>
    """
    from html.parser import HTMLParser

    class Sections(HTMLParser):
        def __init__(self):
            super().__init__()
            self.sections = []
            self.cur = None
            self.tag = None
            self.grab = None  # "h2" | "p" | None
            self.buf = []
            self.skip = 0

        def handle_starttag(self, t, attrs):
            if t in ("script", "style"):
                self.skip += 1
            if t == "section":
                self.cur = {"heading": "", "paras": []}
                self.sections.append(self.cur)
            if t in ("h2", "p") and self.cur is not None:
                self.grab = t
                self.buf = []

        def handle_endtag(self, t):
            if t in ("script", "style") and self.skip:
                self.skip -= 1
            if t == self.grab and self.cur is not None:
                text = " ".join(" ".join(self.buf).split())
                if t == "h2":
                    self.cur["heading"] = text
                elif text:
                    self.cur["paras"].append(text)
                self.grab = None

        def handle_data(self, d):
            if self.grab and not self.skip:
                self.buf.append(d)

    p = Sections()
    p.feed(open(path).read())
    p.close()
    print(f"# OPENER AUDIT — {path}")
    print("# For each: is sentence one the section's claim? "
          "(label/definition/motivation/backstory = FAIL)\n")
    for s in p.sections:
        body = " ".join(s["paras"])
        sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+", body) if x.strip()]
        first = sents[0] if sents else "(no body)"
        last = sents[-1] if sents else "(no body)"
        print(f"heading : {s['heading']}")
        print(f"first   : {first}")
        print(f"last    : {last}")
        print("claim   : ____________________   verdict(S1=claim?): ___\n")


def main(paths):
    if paths and paths[0] == "--imports":
        for p in paths[1:]:
            audit_imports(p)
        return 0
    if paths and paths[0] == "--openers":
        for p in paths[1:]:
            audit_openers(p)
        return 0
    all_hits = []
    for p in paths:
        all_hits += lint_notebook(p)
    for path, cid, loc, name, text in all_hits:
        print(f"{path}  cell={cid}  {loc}  [{name}]  {text}")
    print(f"{len(all_hits)} hit(s)")
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
