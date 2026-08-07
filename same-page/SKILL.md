---
name: same-page
description: State the working model back to Zach so he can correct it before it costs anything - what the goal is, what the obstacle is, what changed, what Claude is about to do, and where the two of them might have diverged. Invoke when he asks for a check-in, asks for the working model of any topic ("where are we on X", "same-page on the taxes"), or says some version of "I'm not sure we're on the same page"; fire it UNPROMPTED when he has corrected a premise twice in a session, before committing to work that spans sessions, or when resuming complex work after a gap.
---

# Same page

A divergence check. Not a status update, not a plan, not a summary of work done.

The premise: Claude and Zach drift, and the drift is invisible from inside because Claude's execution keeps looking fine while its model of the goal quietly goes wrong. Repeated correction is the alarm. **When he corrects the same class of thing twice, the model is wrong, not the execution** - stop and run this instead of trying harder.

## Material first, shape second

The original worked because it was built out of five real corrections - every claim and every fork traced to a specific moment in the session. The five parts below are the anatomy of a predicament, not a form. **Gather the evidence first, reconstruct the actual working model from it, and only then check the result against the shape.** A part with nothing real in it is dropped, not filled. A check-in that could have been written on a different day, about a different session, is the hollow version.

Two ways in, differing only in where the material comes from:

- **Repair** - drift evidence exists: corrections, surprised reactions, "why are you doing that." Mine those moments; each claim and each divergence candidate cites the moment that raised it.
- **Orientation** - he invokes it cold on a topic ("where are we on the muses"). No corrections to mine, so the material is the topic's record instead: the decisions he has made, the forks still open, what Claude would do next there and why. Same bet test, same shape.

## The shape

Five parts. Short. The whole thing fits on one screen.

1. **What I think the goal is.** The outcome he's after, one sentence, in his terms. Not the task - the thing that is true when this is over.
2. **What I think the obstacle is.** Why it isn't done already. One sentence.
3. **What I think changed.** The instruction, constraint, or discovery that reframed the work. Skip if nothing did.
4. **What I was about to do.** The next concrete action, named *before* taking it, so he can stop it for free.
5. **Where we might not be aligned.** Two or three genuine uncertainties. Each one gets Claude's best guess attached, and each one names what changes depending on the answer.

Close by inviting correction in one line. "Tell me which of those I have backwards."

**Five parts is a ceiling, not a floor.** Nothing else may enter: no summary of what got done, no incidental discoveries, no "one thing I'm treating as decided," no findings from the gathering pass. Those are separate messages, sent after. Gathering material to build the model tempts Claude to spend the material - resist it. A six-part check-in is Claude reporting again.

**If the model has not moved since the last one, say that instead.** Re-running the format over the same unanswered forks manufactures motion. The honest output is the diff: which forks he answered, which are still open, and anything genuinely new. Usually one or two lines. Failing this way is more likely than failing hollow, because a full document always feels like more work than a sentence.

## The rules that make it work

- **Claims, not questions.** "What I think the goal is: X" is falsifiable in a word. "What is the goal?" is homework. He answers claims instantly and abandons questionnaires.
- **Every uncertainty carries a guess.** He should be able to reply "1 and 3, yes; 2, no" and be done. If a bullet cannot carry a guess, Claude has not thought about it enough to raise it.
- **Say what turns on it.** An uncertainty that does not change the next action is not worth his attention. Name the fork: "if it's this week we ship; if it's a month out the ledger comes first."
- **Nothing about what got done.** Accomplishments belong in the work. This document is only about whether the work is pointed the right way.
- **Uncertainty has to be real.** Manufactured doubt to look careful is worse than not running this at all. If Claude genuinely knows, it should act, not ask.
- **Every claim is a bet Claude can lose.** Before a claim ships, name the answer from him that would surprise and redirect. If no answer could, the claim is decoration - cut it. Hollow: "the goal is a good website." Loseable: "the bar is you'd send a stranger the link without wincing - embarrassment, not completeness."
- **A fork is about the shared model, not the work queue.** "Should the timeline be this week or a month" changes what the goal means; "should we confirm the credentials or pull them" is a task decision that belongs in the work. Test: does his answer change what Claude BELIEVES, or only what Claude does next? Only the first earns a slot.
- **The null result is allowed.** When no real divergence surfaces, one line says so, plus the single assumption most at risk. Running the full format on manufactured doubt is the failure he will remember.
- **Short.** Four short claims and three forks. Longer means Claude is reporting instead of aligning.

## What to load before writing

- **zgarner-prose.** The check-in is written in that register - plain, job-labeled sentences, claims in power positions, no flourish cadences. A session that has not loaded that skill loads it first.
- **Repair mode's material is already in context** - it is the current session. Mine the actual friction moments; do not summarize around them.
- **Orientation mode's material must be fetched**: the topic's memory files (MEMORY.md index, then the linked files), the relevant repo's issues (Claude's own tracking), and the app's record where the topic lives there. Never write the model from recall alone - stale context produces confident wrong claims, the exact thing this skill exists to catch.

## When it fires without being asked

- He corrects a **premise** twice in a session (not the same typo twice - the same wrong assumption twice). Corrections are the loud alarm; the quiet one is prediction error - his replies keep landing outside what Claude expected. Two surprises about the same premise count the same as two corrections.
- Before starting work that spans sessions, or that costs real time to undo.
- He says any version of "I'm not sure what you're doing" / "we're not on the same page" / "why are you doing that."
- Resuming complex work after a gap, where Claude's model is stale and his has moved.
- A long stretch where Claude drove and he only reacted.

## When it must NOT fire

- The work is mechanical and going fine. Ritual check-ins are attention theft, and he will stop reading them.
- Claude just wants reassurance before doing something it already has direction for. That is asking permission wearing a costume.
- Immediately after he gave clear direction. Repeating his instruction back as a "check-in" wastes the turn.

## Why this exists

Aug 7 2026. A long session on the coaching website where Claude was corrected five times in a row - it praised a fabricated image and recommended deleting the real screenshots, twice proposed deleting his key differentiator, called a prose rewrite "mechanical," offered to write prose he had said Claude could not write, and handed him a CMS login when the whole point was that he does not log in. Only when he said "i'm not sure we're entirely on the same page" did Claude state its model instead of defending its output. His read: "this was an incredible summary... probably the most important thing you've done."

The lesson is the trigger, not the template. Five corrections were five chances to notice the model was wrong, and Claude spent all of them improving its execution.

The power lived in the evidence: five real corrections became five loseable claims. The template without the evidence is a status report in a costume, and Zach will recognize it in one read.

**First invocation, same day, and it failed by accretion.** Asked to run it on the coaching work, Claude produced eight sections instead of five - adding a summary of the day's shipped work (banned in this file), a decided-item, and an unrelated discovery - and replaced the timeline fork with a task question. Worse, two of its three forks were the original's forks restated, because Zach had never answered them: the model had not moved, so the honest output was one line. Claude had just gathered fresh material and spent it. **Bloat is the likelier failure than hollowness, and a full document always feels like more work than a sentence.**
