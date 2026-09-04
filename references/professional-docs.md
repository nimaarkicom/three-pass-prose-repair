# Structural tells: professional documents

Reference material for the `three-pass-prose-repair` skill's non-fiction
route: release notes, PR and issue replies, postmortems, technical
articles, and similar work writing.

Every finding below was checked directly against the paper's own arXiv
page or full text. Where a commonly repeated summary of a paper got a
number, an author name, or a venue wrong, this file uses the corrected
version and says so.

## General checklist (Pass 1 + Pass 2, before any domain rules)

### The seven-category taxonomy from professional editing

Chakrabarty, Laban, Wu (2025), "Can AI writing be salvaged? Mitigating
Idiosyncrasies and Improving Human-AI Alignment in the Writing Process
through Edits" ("LAMP"), CHI 2025, arXiv:2409.14509,
https://arxiv.org/abs/2409.14509. 18 MFA-trained professional writers
made 8,035 real edits across 1,057 LLM-written paragraphs (GPT-4o,
Claude 3.5 Sonnet, Llama 3.1 70B). A seven-category taxonomy covered
all but 10 of the 8,035 edits:

1. **Cliché**: an overused phrase or comparison that has lost its
   impact. The paper's own example, deleted outright by an editor:
   "settled over her like a heavy blanket."
2. **Redundant exposition**: restating something already shown or
   already obvious.
3. **Purple prose**: ornamentation that pulls attention to the writing
   itself rather than the content; long, dense, over-modified
   sentences.
4. **Poor sentence structure**: run-ons and missing transitions. The
   paper's most common fix here was simply splitting one sentence into
   two.
5. **Lack of specificity**: vague, ungrounded statements. This is the
   only category where the professional edit made the passage longer,
   by adding a real, concrete detail.
6. **Awkward word choice**: including a specific tell the paper names:
   "seemed to [verb]" used where the writer isn't actually expressing
   uncertainty. Their own example: "seemed to amplify" edited to
   "amplified."
7. **Tense inconsistency**: tense drifting within a single paragraph
   or sentence.

Measured directly: **74% of edits were replacements, 18% deletions,
8% insertions.** Overwriting was a bigger problem than underwriting.
Edit count correlated negatively with quality: pieces in the
lowest-quality tier got 10.2 edits on average, the highest-quality
tier got 2.4 (Pearson r = -0.31). Awkward word choice and cliché were
the two categories most associated with perceived quality.

**Check:** for each of the seven types, does the draft show it?
**Fix:** default to replacing or deleting over adding new material.
The paper's own automated experiment found LLM editors were good at
trimming purple prose and splitting run-ons, but bad at the two things
that mattered most: writing a genuinely fresh replacement for a
cliché, and adding a detail with real specificity instead of a
generic-sounding one.

### An 11-dimension "slop" taxonomy for factual and semi-formal prose

Shaib, Chakrabarty, Garcia-Olano, Wallace (2025), "Measuring AI
'Slop' in Text," arXiv:2509.19163, https://arxiv.org/abs/2509.19163.
Built a span-level annotation taxonomy from 19 expert interviews, then
had three professional copy editors (15-30 years of experience each)
mark 150 news articles and 100 short QA passages against it. The
taxonomy has three higher-level themes covering 11 dimensions:
**Information Utility** (Relevance, Factuality), **Information
Quality** (Density, Repetition, Templatedness, Coherence, Verbosity),
and **Style Quality** (Bias/subjectivity, Fluency, Word Complexity,
Tone). The dimensions most worth checking by hand:

- **Density**: words that carry no real information for this specific
  context. The paper's own example: "In today's fast-paced modern
  world of cutting-edge technology…"
- **Relevance**: content that doesn't answer the actual question or
  task at hand.
- **Bias/subjectivity**: the inverse of the usual worry. Writing that
  stays falsely neutral where the venue calls for a judgment (a review
  that only lists facts and never evaluates).
- **Templatedness**: a structural formula repeated sentence after
  sentence. The paper's own example: "Dr. X, a researcher at Y, found
  that…" reused across every source cited.
- **Tone**: generic voice with no real personality, or formality
  mismatched to the venue.

The overall "this reads as slop" judgment correlated strongly with how
many separate spans were flagged (Spearman rho = 0.70 for news, 0.51
for short QA). Slop is cumulative, not a single tripwire. Relevance,
Density, and Tone were the three strongest predictors of a document
being judged low quality. And the LLMs tested in this study could not
reliably self-detect their own slop when handed the full taxonomy at
once: precision against the human annotators ranged from 0.08
(zero-shot) to 0.13 (best few-shot condition), recall 0.12-0.19.

**Check:** does every sentence answer the actual question asked? Is
there a paragraph that would read the same in any similar document,
with no fact specific to this one? Is there a place where the venue
calls for a real opinion and the draft stays neutral instead? **Fix:**
cut anything that fails the Density or Relevance test outright; those
two, plus Tone, were the strongest predictors of "reads as slop" in
the study.

### Sentence- and word-level constructs (do this last, in either route)

Reinhart, Brown, Markey, Laudenbach, Pantusen, Yurko, Weinberg (2025),
"Do LLMs write like humans? Variation in grammatical and rhetorical
styles," PNAS 122 (2025) e2422455122, arXiv:2410.16107,
https://arxiv.org/abs/2410.16107. Ran the 66-feature Biber framework
(a standard linguistics tool for grammatical and rhetorical style)
over parallel human and LLM continuations of the same source texts.
Their central finding, stated directly in the paper: instruction
tuning, not model scale, drives the human/AI style gap. A base model
without instruction tuning already writes closer to human style, and
"instruction tuning appears to make the model output less human, not
more."

Constructs GPT-4o used far more than human writing (relative frequency
vs. human = 100%): present participial clauses (about 530%, e.g.
"Leaning on his agility, dances around the ring"), 'that'-clauses as
subject (263%), nominalizations like development/justification (214%),
and "a X of Y and Z" phrasal coordination (194%).

Specific words the same study flagged as overused relative to human
baseline, with exact figures confirmed against the paper: *tapestry*
(appearing in 23% of one model's outputs), *amidst* (27% of outputs),
*camaraderie* (162x human frequency), *underscore* (107x), *intricate*
(119x), *unspoken* (102x), *palpable* and *solace* (95x each).

**Check:** grep the draft for that word list. Count participial-clause
openers ("Leaning on...", "Having considered..."). **Fix:** cut or
replace flagged vocabulary; convert a participial-clause opener to a
plain subject-verb sentence.

### Why word-swaps alone under-perform, even for professional nonfiction

Russell, Karpinska, Iyyer (2025), "People Who Frequently Use ChatGPT
for Writing Tasks Are Accurate and Robust Detectors of AI-generated
Text," ACL 2025, arXiv:2501.15654,
https://arxiv.org/abs/2501.15654. Five frequent LLM users labeled 300
real nonfiction articles; their majority vote missed only one of the
300, including on a set the researchers had already run through an AI
paraphraser specifically to strip surface style. On that paraphrased
set the majority vote hit 100% (zero errors). One specific tell,
unusual or off-key word choice, was flagged *more* often after
paraphrasing than before (69.8% to 88% of labeled examples).
Paraphrasing moved the tell around rather than removing it. A second,
separately "humanized" condition (run through an additional AI
humanizer pass) was still caught by the expert majority vote 100% of
the time; the tells that survived were structural, not lexical: fixed
three-item lists, uniformly upbeat conclusions (the paper's own
example of the pattern: closing on a phrase like "a testament to...a
beacon of hope"), and over-formal quotations and titles.

**Check:** does the piece end on an upbeat, forward-looking note
regardless of what it actually reported? Are there fixed-length lists
of exactly three items in a row? Are quoted statements suspiciously
tidy and complete compared to how people actually talk? **Fix:** let a
postmortem or a technical article's conclusion stay as unresolved as
the actual situation is; vary list length; leave a quote a little
rough if that's how it was actually said.

## Domain-specific rules (Pass 1 + Pass 2, applied on top of the general checklist)

### Release notes and announcements

- Lead with the user-facing effect of the change, not the internal
  process that produced it. A Density violation in the sense above is
  most common here as boilerplate about "our team worked hard to
  deliver."
- Cite the actual PR, ticket, or artifact behind each claim; a claim
  with nothing behind it is the Factuality/specificity gap both LAMP
  and the slop taxonomy flag.
- Cut adjectives that inflate a routine change ("blazing fast,"
  "seamless," "revolutionary") unless a real number backs them. This
  is the Bias/subjectivity code pointed the other way: false
  enthusiasm instead of false neutrality.
- Vary sentence opener and length across entries. A changelog where
  every line starts "Added...", "Fixed...", "Improved..." is the
  templatedness pattern the slop paper measured.

### PR and issue replies, code-review comments

- Answer the actual question in the first sentence. Don't rebuild
  context the reader already has.
- Cite `file:line`, not a paraphrase of the code.
- Cut reflexive praise ("Great question!", "This looks great!"). It is
  the Tone-mismatch failure mode: formal warmth applied regardless of
  what's actually being said.
- Match reply length to what's actually at stake, not to how thorough
  it's possible to sound. A one-line fix deserves a one-line reply.

### Postmortems and incident reviews

- Stay blameless toward the people involved. Stay specific and
  unsparing about the mechanism that failed. A vague, softened cause
  statement is the Density and Bias/subjectivity failures at once: no
  real information, and false neutrality where a plain diagnosis was
  needed.
- Use real timestamps, not "shortly after" or "some time later."
- Include the dead ends that were tried and didn't work, not just the
  fix that succeeded. An inevitable-sounding, linear timeline is the
  same "one tidy causal chain" pattern the fiction research measures,
  applied to what actually happened.
- Give every action item a named owner and a testable condition for
  done, not a passive "we should improve monitoring."

### Technical articles and deep-dive posts

- Open with the actual problem, not scene-setting throat-clearing.
  Russell et al.'s detector-study participants specifically named
  formulaic scene-setting openings as a top tell, and it applies just
  as much to a technical piece that opens with unearned narrative
  color instead of the problem itself.
- Include at least one real dead end or wrong turn taken while solving
  the problem, not just the clean path to the final answer.
- Commit to at least one real, arguable opinion rather than staying
  neutral throughout. See Bias/subjectivity above.
- Attach numbers to conditions ("40ms at p99 under X load"), not bare
  claims ("much faster").

## Full source list for this file

- Chakrabarty, Laban, Wu (2025), "Can AI writing be salvaged?
  Mitigating Idiosyncrasies and Improving Human-AI Alignment in the
  Writing Process through Edits," CHI 2025, arXiv:2409.14509.
- Shaib, Chakrabarty, Garcia-Olano, Wallace (2025), "Measuring AI
  'Slop' in Text," arXiv:2509.19163.
- Reinhart, Brown, Markey, Laudenbach, Pantusen, Yurko, Weinberg
  (2025), "Do LLMs write like humans? Variation in grammatical and
  rhetorical styles," PNAS 122 (2025) e2422455122, arXiv:2410.16107.
- Russell, Karpinska, Iyyer (2025), "People Who Frequently Use ChatGPT
  for Writing Tasks Are Accurate and Robust Detectors of AI-generated
  Text," ACL 2025, arXiv:2501.15654.

Every number above is a measured finding within its own study's
sample. The domain-specific rules that follow from them are this
skill's own editorial judgment, not a tested intervention from any of
the papers.
