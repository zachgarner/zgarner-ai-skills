---
name: zgarner-prose
description: Zach Garner's general technical-writing method — sentence validation by job, power positions, the tell catalog, voice register, truth rules, comment craft. Use for ANY prose an engineer will read that Zach will review — notebooks, docs, decks, chat replies, code comments. The zgarner-fieldeng-template skill layers notebook-specific craft on top of this one.
---

# Zach's prose method

General technical writing to Zach's bar. Two load-bearing pieces:

1. **`references/writing-method.md`** — read fully before writing anything he reviews. Part 1 is the method (job-label sentence validation, power positions, the written opener audit, the review loop, sweep-don't-spot-fix); Parts 2–5 are voice, the tell catalog, truth, and comment craft; Part 6 is where the rules do NOT apply.
2. **`scripts/prose_lint.py <file.ipynb>`** — greps the mechanical tells in markdown and code comments. Run before every hand-back; zero hits or fix them. (`--imports` mode is used by the template skill's show-or-hide audit.)

## The method, in one line

Label every sentence's job (claim / fact / consequence / pointer / gloss / instruction), check the label against its position and the content against the label, run the loop to fixpoint with a WRITTEN audit — the tell blacklist is cleanup, not the method.

## Lexicon

His shorthand for prose problems. When he says one of these, he's naming a specific failure, not venting — match it to the entry and fix that. When he coins a new one, codify it here, in the reference, and in the linter the same day.

- **skeeze** (also "AI skeeze," "skeezy") — performed or salesy prose of any kind: writing that announces, impresses, or sells instead of informing. His most-used tag.
- **grandstanding** — announcing a thing's importance before, or instead of, delivering it: "We built the artifact every later notebook reads." Say what you did, then contextualize. His words for the feeling it gives: "just fucking annoying waste of reading."
- **sandwich** — a verdict, a whispered justification, and a consequence stapled together with dashes: "Memory is easy here — inference keeps no gradients — so each actor runs large batches." Delete the verdict, promote the evidence, keep the consequence.
- **dash inventory** — a finished sentence with a parts list stapled on after a dash. Cut it or promote it to its own sentence; never let it dangle.
- **blah blah blah** — the sentence's shape is noise; the words fill a slot instead of carrying a point. His parody of the punctuation pile: "BLAH BLAH BLAH BLAH: BLAH, BLAH( BLAH BLAH); BLAH."
- **grounded / grounding** — a title or claim tied to the concrete named system, not the abstract category: "GitHub issue process," not "the issue process"; "Journal, Lists, and Day," not "the app is three screens." "Not grounded" means it floats free of anything real.
- **power sentence** — the sentence carrying the actual claim, placed where the eye lands (an opener, a closer, a heading). "I use power sentences": the point itself, no setup, no build-up.
- **punchline setup** (also "staging") — a sentence written to build toward a reveal instead of stating the fact. "I dont punchline setup anything. I speak plainly." Put the facts adjacent and let the difference speak.
