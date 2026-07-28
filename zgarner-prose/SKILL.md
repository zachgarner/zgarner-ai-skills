---
name: zgarner-prose
description: Zach Garner's general technical-writing method — sentence validation by job, power positions, the tell catalog, voice register, truth rules, comment craft. The method is how Zach understands, not only how he writes, so use it for ALL content meant for Zach (chat replies, docs, issues, commit messages, code comments, decks), not only prose he will formally review. The zgarner-fieldeng-template skill layers notebook-specific craft on top of this one.
---

# Zach's prose method

General technical writing to Zach's bar. The method is how he understands, not only how he writes, so it applies to everything written for him, not only prose he'll formally review.

Two load-bearing pieces:

1. **`references/writing-method.md`** — read fully before writing anything for him. Part 1 is the method (job-label sentence validation, power positions, the written opener audit, the review loop, sweep-don't-spot-fix); Parts 2–5 are voice, the tell catalog, truth, and comment craft; Part 6 is where the rules do NOT apply.
2. **`scripts/prose_lint.py <file.ipynb>`** — greps the mechanical tells in markdown and code comments. Run before every hand-back; zero hits or fix them. (`--imports` runs the show-or-hide audit; `--audit` emits the per-sentence worksheet the written review fills in; `--openers` does the same for HTML docs.)

## The method, in one line

Label every sentence's job (claim / fact / consequence / pointer / gloss / instruction), check the label against its position and the content against the label, run the loop to fixpoint with a WRITTEN audit — the tell blacklist is cleanup, not the method.

## Lexicon

His shorthand for prose problems. When he says one of these, he's naming a specific failure, not venting — match it to the entry and fix that. When he coins a new one, codify it here, in the reference, and in the linter the same day.

- **skeeze** (also "AI skeeze," "skeezy") — performed or salesy prose of any kind: writing that announces, impresses, or sells instead of informing. His most-used tag.
- **flowery** — ornate, dressed-up prose that shows off with em-dashes, colons, semicolons, and writerly asides instead of plain statements. Kin to skeeze, but about ornament rather than salesmanship. The fix is plain sentences and earned punctuation.
- **grandstanding** — announcing a thing's importance before, or instead of, delivering it: "We built the artifact every later notebook reads." Say what you did, then contextualize. His words for the feeling it gives: "just fucking annoying waste of reading."
- **sandwich** (a.k.a. **dash sandwich**) — content jammed between two em-dashes in one sentence, breaking its flow. The classic form is a verdict, a whispered reason, then a consequence: "Memory is easy here — inference keeps no gradients — so each actor runs large batches." But any two-dash aside counts, even a definition: "an umbrella issue — a parent issue holding sub-issues — is defined on the issue-process page." Pull the aside into its own sentence. Two in one sentence is always a sandwich. A single dash still has to pass the earned-punctuation bar; he never endorsed asides.
- **dash inventory** — a finished sentence with a parts list stapled on after a dash. Cut it or promote it to its own sentence; never let it dangle.
- **blah blah blah** — the sentence's shape is noise; the words fill a slot instead of carrying a point. His parody of the punctuation pile: "BLAH BLAH BLAH BLAH: BLAH, BLAH( BLAH BLAH); BLAH."
- **grounded / grounding** — a title or claim tied to the concrete named system, not the abstract category: "GitHub issue process," not "the issue process"; "Journal, Lists, and Day," not "the app is three screens." "Not grounded" means it floats free of anything real.
- **power sentence** — the sentence carrying the actual claim, placed where the eye lands (an opener, a closer, a heading). "I use power sentences": the point itself, no setup, no build-up.
- **punchline setup** (also "staging") — a sentence written to build toward a reveal instead of stating the fact. "I dont punchline setup anything. I speak plainly." Put the facts adjacent and let the difference speak.
