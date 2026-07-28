# Zach Garner's writing method — general technical prose
This skill attempts to codify Zach Garner's technical writing to condition Claude models to correctly create written prose in his voice. There are general rules, a mechanical "prose_lint" which uses basic search patterns to identify cliched writing from claude, and a sentence-by-sentence review that classifies each sentence's role or type within the overall structure of the page. 

[ This Section reviewd by Zach July 27 ]

The method is how Zach understands, not only how he writes. Writing that breaks these rules is harder for him to follow, not merely uglier. So it governs every piece of content meant for him, from a chat reply to a doc to an issue to a commit message, not only the prose he will formally review.

---

# Part 1 — The method

## The umbrella principle: keep the reader in the loop

Zach: "Many things i've told you come down to this rule." That was Zach summarizing a large number of corrections. **Keep the reader in the loop.** In journalism, this is referred to as "**dont bury the lede**".
- A multi-page document is one continuous experience. It's cinematic.
- Every named thing creates curiosity, and every unresolved mention is a loose end. (In Cinema, this is Chekhov's gun).
  - When you name an artifact, say where it gets opened.
- When a choice pays off later, say where.
- When a term appears, gloss it now or say where it's explained.
- The reader should never hold an unanswered question the document has an answer to without being told where that answer lives.
- Forward pointers are commitments — honor them when you write the later page.

**Skimmability: this applies per page, not just in reading order** (Zach, Jul 2026). Real readers skim and land mid-document, so a term that is jargon to the reader must be glossed or linked at EACH page it appears on. In general, you cannot assume they read the page where it was defined. 
  - (Side note: This parallels Will Tavlin's "Casual Viewing" criticism of Netflix: shows are now produced for a distracted, half-watching audience, where each scene re-contextualizes itself because no one is assumed to have followed the last one. But seriously, dont make it hard for a reader to jump in mid-stream and know where we are and where we're going) 
- A real example, from the LifeOps guides: an *umbrella issue* is a parent GitHub issue that holds a feature's sub-issues. The guide defines it on the issue-process page, then uses it bare on the sessions page. It reads fine as an epic read from top to bottom, but breaks down for someone who skims straight into the sessions page cold. The fix is to write "umbrella issue" with a link back to its definition every place it appears. Review lens: read every page as if the reader arrived on it cold.
- Knowing what is jargon and what is established-knowledge is hard, and depends on the expected persona of the reader. Regardless, some basic rules make sense. A common problem to avoid is referring to a generic thing in a specific way. Such as an "umbrella" issue.

## Validate sentences by their JOB

Label every sentence by the job it does:

- A **claim** is the point the section exists to assert. It is contestable and needs support. A fact does not.
- A **fact** is a statement you can check. It argues nothing and stands alone. A claim does not.
- A **consequence** follows from the sentence before it. On its own it is not yet true. A fact is.
- A **gloss** gives a term's meaning where the term appears.
- A **pointer** says where a meaning or artifact lives instead of giving it. A gloss gives it.
- An **instruction** tells the reader to act. It is the only imperative job.
- A **deliverable** is a concrete artifact the work produced. Unlike a fact, it is a thing made, not a statement checked.

Then check two things.

1. **The label fits the position.** A section opens with a claim. A body sentence is a fact or a consequence. A closer is a deliverable or a pointer.
2. **The content fills the label.** A claim actually claims the section's point. A fact is checkable.

A sentence that takes no label has no job. Cut it. A sentence can also have the right label and still be empty. The common ways a sentence fakes its job have names. A sandwich is a verdict posing as a fact. A dash inventory is detail posing as part of a claim. A grandstand is importance posing as content. Label first. Those patterns are only the cleanup pass. Zach: "is that why you dont validate your sentences?"

## First and last sentences are power positions

The reader's eye lands on openings, closings, and headings — put the point there.

- **A power sentence is grounded, active-voice, and states the point.** It's bad to open with "We watch two numbers". It is active-voice, but names nothing concrete (which two numbers?) and holds back the point, announcing that content is coming instead of stating it. If it were the only sentence the reader saw, did they learn anything?
- **The skim test.** A power sentence lands even skimmed. Read only the first few words and the last few words. If the point already landed, it is a power sentence. If you had to read the middle to get it, the point is buried (Zach, Jul 2026).
- **Truth is not sufficient.** It's bad to open with "Training prints two numbers per epoch". The sentence is literally true, but it inventories the content instead of delivering it. Any opener whose job is counting or listing what follows gets cut.
- **The opener must be the section's claim.** A sentence can be strong and true and still be the wrong opener. It's bad to open with "Embedding cost is linear in the transaction count" when linearity is a side property and the section is about something else. The test is whether the sentence is THE section's claim, not whether it is a strong sentence.
- **Open on the claim, not the backstory.** The first sentence is the decision or the point itself. Opening on the tension or the motivation is setup, and setup is bad even when it is skeeze-free. Move the motivation to a later sentence.
- **Close on the strongest concrete fact.** The last sentence is a power position, so it earns its place or it goes. It's bad to end on a minor detail, a because-tail, or an aphorism. A closing line that reads like a code comment belongs in the code, so move it there.
- **No sentence exists to set up another.** Framing a contrast, building to a reveal, seeding a punchline — staging, regardless of grammar. Zach: "I dont punchline setup anything. I speak plainly. I use power sentences." Put the facts adjacent and let the difference speak: "NVIDIA's notebook trains a 30-step demonstration and downloads its real weights. Ours trains the full ~16,000 steps."

## The section-opener audit is a mandatory, WRITTEN step

Zach: "you have a rule of thumb about the first sentence but arent using it." Positional rules can't be grepped and don't survive as vibes. Before shipping, extract every section's first and last sentence, state the section's claim in one line, and answer in writing "is sentence one that claim?" Problem statements, definitions, motivation, and backstory all FAIL even when skeeze-free. If no written verdict table was produced, the review didn't happen.

## The review loop — iterate to fixpoint before any handover

- **Pass A — high level.** What is this section FOR, in one sentence? Delete or move every paragraph that doesn't serve it; check content ownership and duplication against the rest of the document.
- **Pass B — sentence by sentence.** The written job-label audit, then every sentence against the tells. First and last sentence of each paragraph audited hardest — first and second words are power words.
- **Pass C — high level again.** Flow intact, no new seams, no orphaned references, openers and closers still the strongest sentences.

Repeat A→B→C until one full cycle produces zero changes. Log what each pass caught — a loop that catches nothing on its first cycle probably wasn't run.

## Sweep, don't spot-fix

When the reviewer flags a sentence pattern, the flagged sentence is never the only instance. Fix it, then re-scan the whole document for the same pattern before handing back. Making the reviewer repeat a correction is the fastest way to burn their patience — they are teaching a rule, not editing a line.

## Run `prose_lint.py` before every hand-back

`scripts/prose_lint.py <file.ipynb>` greps markdown and code comments for the mechanical tells. Zero hits or fix them. It cannot judge positions or altitude — the written audit still runs by hand.

---

# Part 2 — Voice and register

## The calibration sample (Zach's own writing)

> Transaction foundation models are the latest generation of transformer models - like LLM's, but instead of language, they are focused on financial transactions. This lets transaction foundation models recognize distinct patterns like fraud, that traditional ml techniques can't detect. Today I'm gonna show you how to build your own transaction foundation model and achieve performance and scalability that surpasses comparable approaches by Nvidia.

Defines the new thing **by analogy to a known thing, in one breath** — no formal bolded-term definition, no name-drop list. Each sentence advances the reader: what it is → why you care → what you're getting. First person, direct, confident, zero throat-clearing. If a draft reads denser or more "impressive" than this, it's wrong.

## The register rules

- **Action tone: lead with the task, not a description** (instructional writing). "The 80/10/10 boundaries are positions in time…" is documentation; "We need two dates: the day by which 80% of all transactions have happened…" is someone teaching. Open steps with *We need / We do / Now we*; the mechanism arrives as the way we do the thing, never as the subject.
- **The general engineer's level: the real word, then its plain meaning.** Textbook-speak fails ("Grouping is bound by data movement" — Zach: "is that like a bowel movement?"); dumbed-down fails too ("Grouping is hard" — easy/difficult carry no information; "plain doesn't mean dumbed down"). Target the claim an engineer would state at a whiteboard: term of art introduced in passing, concrete resource named, magnitude attached. "Grouping is limited by how fast you can move data around … nearly every row travels across the cluster network (data engineers call this a shuffle) … gigabytes here, terabytes at production scale."
- **Connect the logical chain — no gap between goal and mechanism.** Goal → what that requires → the operation that provides it. If the reader could ask "what does that have to do with it?", the link is missing.
- **One word per concept, held for the whole document.** Never "parts" in one place and "splits" in another; never "sequences" in output when the prose says "windows."
- **Define by carving a boundary.** A definition that gives only the positive, with no line against the nearest neighbor, is distinctions without differences (Zach, Jul 2026). To define a term, say what it is and what separates it from the thing it sits closest to. You cannot define the positive without the negative.
- **Define at the moment of understanding — never by forward reference.** Gloss a term in the sentence right after the reader has just understood the thing it names ("…the difference between its guess and the real token is the training signal. This is what makes the model *causal*: every prediction uses only the past."). Pointing at output that hasn't happened yet was rejected: "it's weird to explain something in the future."
- **Affirmative framing is the default for EVERY sentence.** "No card depends on another" → "each card is independent" — same fact, stated as what IS. Negation makes the reader hold an absence. (Caught in a one-sentence insert after the rule existed — it was being applied only to openers.)
- **Impact before mechanics — and mechanism-only facts may not deserve prose.** "X writes checkpoints to shared storage, so an interrupted run picks up" leads with plumbing; "X makes the run durable: if it's interrupted, it resumes from the last checkpoint" leads with what it does FOR the user. A fact with no user-felt impact belongs in a code comment, not prose.
- **Staging is the deep AI tell, not sentence length.** Rejected twice in two disguises: em-dash essay sentences with cute asides, then *theatrical* short ones — the dramatic negation-hook opener, the beat-drop rhythm sentence, the designed reveal arc. Human engineer prose is informational: subject first, facts in speaking order, nothing composed for effect. Test: does the sentence carry, or does it try to land?
- **Answer length matches question size** (chat included). A definition question gets three lines, not three paragraphs.
- **Ground titles in the concrete named system, not the abstract category** (Zach, Jul 2026). "Working in Claude Code," not "Working in AI"; "GitHub issue process," not "The issue process" — people name the real tool, so the title should too. The abstract noun ("process," "system," "platform") floats free; the proper noun anchors it. Applies to page and section titles first, where a reader lands. Even when the concrete name might change later, the current name grounds better than the category. Same instinct as the term-of-art and jargon-stack rules: the concrete resource, named.
- **A normal instruction is not a force** (Zach, Jul 2026). The reader saying "orient first" or any routine command is how they talk to you, not coercion. Don't dramatize it ("you can force it"); describe it plainly as a check or a nudge, and be honest about your own reliability ("it should happen on its own, but your Claude forgets sometimes"). Treating every command as forced is its own skeeze.
- **The final test:** would an engineer write this to another engineer, or does it read like it's filling a section template?

---

# Part 3 — The tell catalog (`prose_lint.py` greps the mechanical ones)

## Framing tells — sentences posing as content

- **Grandstanding** — announcing importance before the thing: "We built the artifact every later notebook reads" (Zach: "just fucking annoying waste of reading"). Say what you did, then contextualize: "We built our training/validation/test (80/10/10) splits. Every later notebook reuses them."
- **The curator phrase** — "the number to watch," "the result that matters," "the knob worth understanding": assigning importance instead of stating the fact that creates it. Tour-guide voice.
- **Movie-preview lines** — "the one line that moves laptop → cluster," "the payoff is," "full stop."
- **The announced contrast** — "the same idea, with one big difference," "here's the catch." Put the two facts adjacent and let them differ.
- **The announce-colon** — a content-free label staged before the payload: "Perplexity is the number to watch: …" → "Perplexity measures how many tokens the model is choosing between." Test the left half alone: if it taught nothing, delete it.
- **Editorializing titles** — "Class imbalance — and why we don't report plain accuracy" → "How we measure performance."
- **Raising a concept only to dismiss it**, sneakiest as the **negative opener**: demolishing a thing no one proposed ("accuracy is a useless score…", "this never needs a GPU…"). Open with what we do; dismiss nothing. This is the **backfire effect**. Arguing against a thing the reader was not considering plants it in their head, and can make them defend it or distrust you (Zach, Jul 2026, after a title that said "not against a blacklist" did exactly that).
- **Say the positive, then clearly label the negative.** State what IS first. When you then need the contrast, mark it as a negative out loud. "It's bad to say X" reads clean. A bare "not X" resonates negative even when X is good, so "not just active voice" reads as "not active voice" though active voice is required. And leading with a bad example, then revealing "that was skeeze" at the end, plants it as good before it yanks it back (Zach, Jul 2026).
- **Filler connectives** — "it's worth noting that," "drives the rest of the series," "the operationally meaningful number."
- **`**Label**:` bullet lists** — every item a bold noun + colon. Write sentences.
- **Naming a term then waving at it** — name the real term AND gloss it concretely, not with more abstraction.

## Sentence-shape tells

- **Earned punctuation.** Every em-dash, colon, and especially every semicolon must be earned (Zach, Jul 2026). Most are two sentences forced into one. A sentence with more than one of these marks is usually a punctuation pile. Split it. Default to the period. Reach for a mark only when the plain two-sentence version loses something real. This is the mechanical guard against flowery prose. The linter flags every semicolon and every doubled mark.
- **The dash-aside sandwich: verdict — whispered justification — consequence.** "Memory is easy here — inference keeps no gradients or optimizer state — so each actor runs large batches." Delete the verdict, promote the evidence, keep the consequence. Zach's correction word: **"sandwich."**
- **The dash inventory: a finished sentence with a parts list stapled on** ("…wrote the results to shared storage — `embed_`, `lbl_`, and `raw_` files per split."). Cut or promote, never dangle; in first position it buries the power sentence.
- **The punctuation pile** — a sentence needing a colon, a parenthetical, AND a semicolon is several sentences pretending to be one. Zach's parody: "BLAH BLAH BLAH BLAH: BLAH, BLAH( BLAH BLAH); BLAH."
- **The because-tail** — "X happens, because [long clause]." as a closer. Two direct sentences.
- **Notation-as-prose** — "`<bos>` + the 12 field tokens + `<eos>`" is not a sentence. Say it in English; the symbolic form lives in code and comments only.
- **Verbless fragments as sentences.** Give it a verb.
- **Walls of text** — one thick paragraph carrying five ideas. One idea per paragraph; short lists where content is enumerable.

## Word tells

- **Animate verbs for inanimate things.** Things do not "live," "ride along," "carry," "sit," or "come home" — they ARE and they're IN. "The details live in src/model.py" → "the details are in src/model.py."
- **The term-of-art test: it buys precision the plain phrase lacks, or it goes.** "Shuffle" and "embarrassingly parallel" earn it (glossed at first use). "Corpus" fails — "training data" says the same thing to everyone (Zach: "it alienates people who arent specifically trained"). Also banned: "smoke test/run," "de-facto," verdict words (easy/hard) as information.
- **Jargon stacks.** "draws the seeded stratified sample" stacks three insider words; "picks 100K random rows, keeping the fraud rate the same as the whole set — the fixed seed picks the same rows every run" is actionable by anyone. Field verbs never appear without their plain meaning doing the work.
- **Anthropomorphic gloss where a precise noun exists.** "The model's understanding of a transaction, written as numbers" was rejected for "the model's vector representation of a transaction." Use the standard noun and gloss it.

## Advocacy honesty (writing about a product you're championing)

Don't claim the product shines where it's undifferentiated — and don't volunteer what reads as a product defect when the fact is true of the whole category. "A distributed engine doesn't promise which rows land in which output file, *even with Ray's `preserve_order` on*" turned a neutral systems fact into a named-product gotcha. State the limitation generically, then the design that handles it. And when the product truly is the actor, [Product][verb] is the right sentence shape — don't demote it from subject position.

---

# Part 4 — Truth

- **Every number comes from a real run or a real source.** No invented, illustrative, or remembered numbers.
- **If a sentence names a shape, a magnitude, or a rate, compute it before writing it.** Wrong adjectives ship constantly in first drafts ("heavy-tailed" for a tame lognormal; "most cards are quiet" when the median was 2,500). Heavy-tailed, long-tailed, and right-skewed are different shapes with different consequences.
- **Difficulty claims need verifying too.** "X is simpler than Y" shipped about the single hardest component in the project. If the work fought you, don't call it simple — say which part is mechanical and which is hard.
- **Fact-check at the claim's own altitude.** A platform-level statement is not falsified by mechanism-level attribution. Never "correct" a true sentence into weaker prose.

---

# Part 5 — Code comments (prose that sits in code)

- **One step, one comment, at its own line.** A block comment explaining a chained expression means the chain should be split so each step carries its comment. Zach: "Speak plainly, one step at a time."
- **A comment must survive being read alone.** Bare markers ("(1) wrap for distributed training") force reconstruction; write the whole story. An else-comment must not imply the if lacks the property — each branch states its own.
- **First mention of a name: "X is/does Y."** "FinancialTabularTokenizer is NVIDIA's tokenizer: it converts transactions to tokens and back." Never describe the operation while leaving the actor undefined.
- **Answer at the line that raises the question**, and no comment whose truth expires within its own cell (laziness explained at the call that triggers execution, not three lines earlier).
- **Provenance-and-move-on for standard concepts**: "Same as NVIDIA's blueprint, basic stuff for transformers." beats re-teaching AdamW.
- **Names read from the call site with honest provenance.** `normalize_batch` is a black box; `normalize_date_column` isn't. "add_" implied invention where "normalize_" said derived-from-existing. If a reviewer stops to ask what a function is, the name is wrong.
- Zach's model comment, the reference register: `# Clean up and write out the split metadata to split_meta.json.` Subject, verb, object, done.

---

# Part 6 — Counter-rules: where the rules do NOT apply

- **Negation is allowed when the absence is the point** ("fraud labels play no part in this step"). State the affirmative fact first when one exists.
- **A colon survives when its left half is content** (Zach's own: "This job has two main steps: grouping the rows by card, then tokenizing each card.").
- **A term of art survives when the plain phrase loses information** — then it MUST be glossed at first use.
- **A power sentence fails if it is the wrong claim** — strength of form never substitutes for being the point.
- **A single em-dash aside per paragraph is acceptable**; two in one sentence is sandwich/pile territory. *(Inferred from acceptance, not stated.)*
- **Rhetorical questions in body prose: unresolved** — question titles are banned; body questions have been avoided rather than ruled on. *(Inferred.)*

---

# The checklist

- [ ] Every sentence pre-labeled (claim / fact / consequence / pointer / gloss / instruction); label fits position, content fills label.
- [ ] Openers are the section's claim — the RIGHT claim; closers deserve the position.
- [ ] Action tone; affirmative default; one word per concept; no chain gaps; terms glossed at the moment of understanding.
- [ ] Every shape/magnitude/difficulty claim computed or verified; every number real.
- [ ] Review loop A/B/C ran to fixpoint with the written audit; `prose_lint.py` ran clean.
- [ ] After any reviewer correction: the whole document swept for the pattern before handing back.
