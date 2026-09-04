# Professional documents: what the research measures

Reference material for the `three-pass-prose-repair` skill's non-fiction
route: release notes, PR and issue replies, postmortems, technical
articles, and similar work writing. Fiction's architecture problem shows up
here as an information and honesty problem instead: filler that carries no
signal, false neutrality where a plain judgment was needed, and a
structure that ignores what the document is actually for. Same three-pass
order as the fiction route; this file covers a general checklist plus
domain-specific rules. Every number below was read directly from the
paper's own text, not from another project's summary of it. Where a
common secondhand summary of one of these papers gets a number or an
author name wrong, this file uses the corrected version and drops
anything that could not be directly confirmed.

## General checklist (Pass 1 and Pass 2, before any domain rules)

### The seven edit types professional writers actually make

[Chakrabarty, Laban, Wu (2025), "Can AI Writing be Salvaged? Mitigating
Idiosyncrasies and Improving Human-AI Alignment in the Writing Process
through Edits," CHI 2025, arXiv:2409.14509
](https://arxiv.org/abs/2409.14509) had 18 professional, MFA-trained
writers make 8,035 real edits across 1,057 LLM-written paragraphs (from
GPT-4o, Claude 3.5 Sonnet, and Llama 3.1 70B), then built a seven-category
taxonomy from those edits:

1. **Cliche**: an overused phrase or comparison. The paper's own example:
   "a tapestry of modernity threaded with the hum of traffic," deleted
   outright.
2. **Redundant exposition**: restating something already shown or already
   obvious.
3. **Purple prose**: ornamentation that pulls attention to the writing
   itself rather than the content; long, dense, over-modified sentences.
4. **Poor sentence structure**: run-ons and missing transitions. The most
   common fix here was simply splitting one sentence into two.
5. **Lack of specificity**: vague, ungrounded statements. The only
   category where the professional edit made the passage longer, by
   adding a real, concrete detail.
6. **Awkward word choice**: including one specific tell the paper singles
   out: "seemed to amplify" corrected to "amplified," a hedge inserted
   where the writer wasn't actually expressing uncertainty.
7. **Tense inconsistency**: tense drifting within a single paragraph or
   sentence.

Editors' actual edit mix, measured directly: **74% replacement, 18%
deletion, 8% insertion.** Overwriting was a far more common problem than
underwriting. The number of edits a paragraph received correlated
negatively with its rated quality (r = -0.31): better paragraphs needed
fewer fixes. Writer-edited paragraphs were preferred over both raw LLM
output and an automated LLM-editor's version in a follow-up ranking study
(average rank 1.47 for writer-edited, 1.99 for LLM-edited, 2.55 for raw
LLM output, Wilcoxon p = 2.8e-13). All three source LLMs converged on
similar idiosyncratic phrasing regardless of which model wrote the
original paragraph, phrases close to "weight of," "sense of," and
"unspoken" recurred across all three.

**Check:** for each of the seven types, does the draft show it? **Fix:**
default to replacing or deleting over adding new material. The paper's own
automated-editing experiment found LLM editors were reasonably good at
trimming purple prose and splitting run-ons, but consistently worse than
human editors at the two things that mattered most: writing a genuinely
fresh replacement for a cliche instead of swapping one flat phrase for
another, and adding a detail with real specificity instead of a
generic-sounding one.

### The taxonomy for factual and semi-formal prose

[Shaib, Chakrabarty, Garcia-Olano, Wallace (2025), "Measuring AI 'Slop' in
Text," arXiv:2509.19163](https://arxiv.org/abs/2509.19163) built a
span-level annotation taxonomy from 19 expert interviews (NLP researchers,
professional writers, journalists, linguists), then had professional copy
editors mark 150 news articles and 100 short QA answers against it. The
paper defines seven core codes: Density, Relevance, Factuality, Bias,
Repetition, Templatedness, Coherence. It also separately measures four
additional style dimensions on the same texts: Tone, Fluency, Verbosity,
and Word Complexity, for eleven measured dimensions in total.

- **Density**: words that carry no real information for this specific
  context.
- **Relevance**: content that doesn't answer the actual question or task
  at hand.
- **Factuality**: errors, invented specifics, or subtly wrong claims.
- **Bias**: the presence or absence of a subjective or evaluative
  perspective the venue actually calls for, meaning writing that stays
  falsely neutral where a real judgment was needed, as much as writing
  that is one-sidedly slanted.
- **Repetition**: the same word or phrase reused past the point of intent.
- **Templatedness**: a structural formula repeated sentence after
  sentence, an example being the same "Dr. X, a researcher at Y, found
  that..." construction reused for every source cited.
- **Coherence**: whether the piece holds together as a single, logically
  connected text rather than a set of loosely joined statements.

Measured findings worth acting on directly: the overall "this reads as
slop" judgment correlated strongly with how many separate spans were
flagged in a document (Spearman rho = 0.70 for news articles, 0.51 for
short QA answers). Slop is cumulative, not a single tripwire. Across a
regression over the whole dataset, the three strongest predictors of a
document being judged low quality were Relevance, Density, and Tone (each
a significant positive predictor, coefficients 0.06, 0.05, and 0.05
respectively); all seven core codes were significant positive predictors
on their own. Separately, and importantly: **the LLMs in this study could
not reliably self-detect their own slop.** GPT-4 run zero-shot on the full
annotation guide agreed with the human annotator at close to chance
(Cohen's kappa about 0.01), and span-level extraction precision was only
around 0.14.

**Check:** does every sentence answer the actual question asked? Is there a
paragraph that would read the same in any similar document, with no fact
specific to this one? Is there a place where the venue calls for a real
opinion and the draft stays neutral instead? **Fix:** cut anything that
fails the Density or Relevance test outright; those two, plus Tone, were
the strongest predictors of "reads as slop" in this study.

### Sentence- and word-level constructs (do this last, in either route)

[Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg, Brown (2025), "Do
LLMs write like humans? Variation in grammatical and rhetorical styles,"
PNAS, arXiv:2410.16107](https://arxiv.org/abs/2410.16107) ran the
66-feature Biber framework, a standard linguistics tool for grammatical
and rhetorical style, over parallel human and LLM continuations of the
same source texts. Their central finding is that instruction tuning, not
model scale, drives the style gap: the paper points to "the apparently
central role of instruction tuning in creating these discrepancies between
human and model generated text," and notes that larger instruction-tuned
models show close to the same gap as smaller ones.

Constructs the LLM outputs used far more than human writing (relative
frequency versus human = 100%, effect size d in parentheses): present
participial clauses 530% (d=1.38, example: "leaning on his agility,
dances around the ring"), 'that'-clauses as subject 260% (d=0.77),
nominalizations such as development/justification 210% (d=1.23), and "a X
of Y and Z" phrasal coordination 190% (d=0.81).

Specific words the same study flagged as heavily overused relative to
human baselines: camaraderie (162x human frequency), tapestry (155x,
appearing in 23% of one model's outputs), intricate (119x), underscore
(107x), unspoken (102x), amidst (100x, in 27% of outputs), and palpable
and solace (95x each).

**Check:** grep the draft for that word list. Count participial-clause
openers ("Leaning on...", "Having considered..."). **Fix:** cut or replace
flagged vocabulary; convert a participial-clause opener to a plain
subject-verb sentence.

### Why word-swaps alone under-perform, even for professional nonfiction

[Russell, Karpinska, Iyyer (2025), "People Who Frequently Use ChatGPT for
Writing Tasks Are Accurate and Robust Detectors of AI-generated Text," ACL
2025, arXiv:2501.15654](https://arxiv.org/abs/2501.15654) had five
frequent LLM users label 300 real nonfiction articles. The paper's own
wording: "the expert majority vote misclassifies only 1 of 300 articles,"
roughly 99.7% correct, including on a set the researchers had already run
through an AI paraphraser specifically to strip surface style. The expert
majority vote reached 100% accuracy on that paraphrased condition,
described in the paper as robust to paraphrasing specifically. A separate
humanized condition (run through an additional AI "humanizer" pass) was
still caught by the expert majority vote 100% of the time; one specific
surviving tell tied directly to humanization was a heavier use of formal
titles ("Dr.", "Prof.") before a person's name than genuinely human-written
articles used. Annotators separately named several other recurring tells
in their own reasoning across the study: "the tendency of LLMs to always
list examples in groupings of three," a fixed "it's not just this, it's
this" construction, conclusions that read as "a beacon of hope and
inspiration" regardless of the actual subject, and quoted speech that
"sound[s] overly formal" and mirrors the surrounding article's style too
closely to read as something a real person actually said.

**Check:** are there fixed-length lists of exactly three items in a row?
Does the piece end on an upbeat, forward-looking note regardless of what it
actually reported? Are quoted statements suspiciously tidy and formal
compared to how people actually talk? **Fix:** vary list length; let a
postmortem or technical article's conclusion stay as unresolved as the
actual situation is; leave a quote a little rough if that is how it was
actually said.

## Domain-specific rules (Pass 1 and Pass 2, applied on top of the general checklist)

### Release notes and announcements

- Lead with the user-facing effect of the change, not the internal process
  that produced it. Boilerplate about "our team worked hard to deliver" is
  a Density violation in the sense above.
- Cite the actual PR, ticket, or artifact behind each claim; a claim with
  nothing behind it is the Factuality/specificity gap LAMP and the slop
  taxonomy both flag.
- Cut adjectives that inflate a routine change ("blazing fast,"
  "seamless," "revolutionary") unless a real number backs them. This is
  the Bias code pointed the other way: false enthusiasm instead of false
  neutrality.
- Vary sentence opener and length across entries; a changelog where every
  line starts "Added...", "Fixed...", "Improved..." is the Templatedness
  pattern the slop study measured.

### PR and issue replies

- Answer the actual question in the first sentence. Don't rebuild context
  the reader already has.
- Cite `file:line`, not a paraphrase of the code.
- Cut reflexive praise ("Great question!", "This looks great!"). It is the
  Tone-mismatch failure mode: formal warmth applied regardless of what is
  actually being said.
- Match reply length to what is actually at stake, not to how thorough it
  is possible to sound. A one-line fix deserves a one-line reply.

### Postmortems

- Stay blameless toward the people involved, and be specific and unsparing
  about the mechanism that failed. A vague, softened cause statement is
  both a Density and a Bias failure at once: no real information, and
  false neutrality where a plain diagnosis was needed.
- Use real timestamps, not "shortly after" or "some time later."
- Include the dead ends that were tried and didn't work, not only the fix
  that succeeded. An inevitable-sounding, linear timeline is the same "one
  tidy causal chain" pattern found in fiction, applied to what actually
  happened.
- Give every action item a named owner and a testable condition for done,
  not a passive "we should improve monitoring."

### Technical articles and deep-dive posts

- Open with the actual problem, not scene-setting. A formulaic
  scene-setting opening applies just as much to a technical piece that
  opens with unearned narrative color instead of the problem itself.
- Include at least one real dead end or wrong turn taken while solving the
  problem, not only the clean path to the final answer.
- Commit to at least one real, arguable opinion rather than staying
  neutral throughout. See the Bias code above.
- Attach numbers to conditions ("40ms at p99 under X load"), not bare
  claims ("much faster").

## Full source list for this file

- Chakrabarty, Laban, Wu (2025), "Can AI Writing be Salvaged? Mitigating
  Idiosyncrasies and Improving Human-AI Alignment in the Writing Process
  through Edits," CHI 2025, arXiv:2409.14509.
  https://arxiv.org/abs/2409.14509
- Shaib, Chakrabarty, Garcia-Olano, Wallace (2025), "Measuring AI 'Slop' in
  Text," arXiv:2509.19163. https://arxiv.org/abs/2509.19163
- Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg, Brown (2025),
  "Do LLMs write like humans? Variation in grammatical and rhetorical
  styles," PNAS, arXiv:2410.16107. https://arxiv.org/abs/2410.16107
- Russell, Karpinska, Iyyer (2025), "People Who Frequently Use ChatGPT for
  Writing Tasks Are Accurate and Robust Detectors of AI-generated Text,"
  ACL 2025, arXiv:2501.15654. https://arxiv.org/abs/2501.15654

As with the fiction reference file, every number above is a measured
finding within its own study's sample; the domain-specific rules that
follow from them are this skill's own editorial judgment, not a tested
intervention from any of the papers.
