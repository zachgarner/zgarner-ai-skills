# zgarner-ai-skills

Zach Garner's Claude Code skills, kept in one place so they survive across
machines, repos, and worktrees instead of getting stranded on a local branch.

Each top-level directory is one skill (a `SKILL.md` plus its references and
scripts). Point Claude Code at them by symlinking each into your skills
directory.

## Skills

- **[zgarner-prose](zgarner-prose/)** — general technical-writing method to
  Zach's bar: label every sentence's job, put the claim in the power positions,
  ground titles in the concrete named system, and sweep for the tell catalog.
  Ships with `prose_lint.py` (mechanical tells + an `--openers` audit mode).
- **[zgarner-fieldeng-template](zgarner-fieldeng-template/)** — the
  notebook-specific layer on top of zgarner-prose for Anyscale demo templates:
  what to show vs hide, Ray visibility, notebook structure, outputs, and the
  collaboration protocol. Requires zgarner-prose.

## Install

Clone once, then symlink the skills you want into your user skills directory so
they load in every session:

```sh
git clone https://github.com/zachgarner/zgarner-ai-skills.git ~/zx/zgarner-ai-skills
mkdir -p ~/.claude/skills
ln -s ~/zx/zgarner-ai-skills/zgarner-prose ~/.claude/skills/zgarner-prose
```

Use a project's `.claude/skills/` instead of `~/.claude/skills/` to scope a
skill to one repo. Pulling this repo updates the skill everywhere it's linked.
