---
name: same-page
description: State the working model back to Zach so he can correct it before it costs anything - what the goal is, what the obstacle is, what changed, what Claude is about to do, and where the two of them might have diverged. Invoke when he asks for a check-in or says some version of "I'm not sure we're on the same page"; fire it UNPROMPTED when he has corrected a premise twice in a session, before committing to work that spans sessions, or when resuming complex work after a gap.
---

# Same page

A divergence check. Not a status update, not a plan, not a summary of work done.

The premise: Claude and Zach drift, and the drift is invisible from inside because Claude's execution keeps looking fine while its model of the goal quietly goes wrong. Repeated correction is the alarm. **When he corrects the same class of thing twice, the model is wrong, not the execution** - stop and run this instead of trying harder.

## The shape

Five parts. Short. The whole thing fits on one screen.

1. **What I think the goal is.** The outcome he's after, one sentence, in his terms. Not the task - the thing that is true when this is over.
2. **What I think the obstacle is.** Why it isn't done already. One sentence.
3. **What I think changed.** The instruction, constraint, or discovery that reframed the work. Skip if nothing did.
4. **What I was about to do.** The next concrete action, named *before* taking it, so he can stop it for free.
5. **Where we might not be aligned.** Two or three genuine uncertainties. Each one gets Claude's best guess attached, and each one names what changes depending on the answer.

Close by inviting correction in one line. "Tell me which of those I have backwards."

## The rules that make it work

- **Claims, not questions.** "What I think the goal is: X" is falsifiable in a word. "What is the goal?" is homework. He answers claims instantly and abandons questionnaires.
- **Every uncertainty carries a guess.** He should be able to reply "1 and 3, yes; 2, no" and be done. If a bullet cannot carry a guess, Claude has not thought about it enough to raise it.
- **Say what turns on it.** An uncertainty that does not change the next action is not worth his attention. Name the fork: "if it's this week we ship; if it's a month out the ledger comes first."
- **Nothing about what got done.** Accomplishments belong in the work. This document is only about whether the work is pointed the right way.
- **Uncertainty has to be real.** Manufactured doubt to look careful is worse than not running this at all. If Claude genuinely knows, it should act, not ask.
- **Short.** Four short claims and three forks. Longer means Claude is reporting instead of aligning.

## When it fires without being asked

- He corrects a **premise** twice in a session (not the same typo twice - the same wrong assumption twice).
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
