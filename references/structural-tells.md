# Structural tells: fiction and narrative essays

Reference material for the `three-pass-prose-repair` skill's fiction
route. Each check below names the study it came from, the actual
measurement, and what to do about it. Treat every "human vs. AI"
number as a moderate target, not a pole to invert toward. See
Calibration in the main `SKILL.md`.

Every finding below was checked directly against the paper's own
arXiv page or full text, not against another project's summary of it.
Two of the studies below turned out to carry a wrong author list in
earlier secondhand write-ups; this file uses the corrected author
list and says so.

## Pass 1: architecture

### 1. The narrator explains the theme instead of trusting the plot

Russell, Rajendhran, Pham, Iyyer, Wieting (2026), "StoryScope:
Investigating idiosyncrasies in AI fiction," arXiv:2604.03136,
https://arxiv.org/abs/2604.03136. Built a pipeline that extracts 304
narrative-structure features across 10 dimensions from 61,608 stories
(10,272 prompts, each answered by one human author and five LLMs).
"Narratorial Thematic Commentary," the narrator or a character
stepping outside the story to state its lesson, appeared in 77% of
AI-written stories versus 52% of human-written ones. Dialogue used as
a vehicle for philosophical debate followed the same pattern: 59% AI
versus 34% human.

**Check:** does any line say, in effect, what the story is "about"?
Does a conversation exist mainly to state a position rather than move
the scene forward? **Fix:** cut the line. Let the reader infer meaning
from what happened, not from being told.

### 2. One tidy causal chain, no subplot, no loose thread

StoryScope again: "Subplot Integration to no subplots" appeared in 79%
of AI stories versus 57% of human stories. The paper's own summary of
its central pattern: AI stories "over-explain themes and favor tidy,
single-track plots," while human stories "frame protagonist's choices
as more morally ambiguous and have increased temporal complexity."

Independently, Xu, Jojic, Rao, Brockett, Dolan (2025), "Echoes in AI:
Quantifying Lack of Plot Diversity in LLM Outputs," PNAS 122 (2025),
arXiv:2501.00273, https://arxiv.org/abs/2501.00273, measured how
inevitable a plot turn is by resampling the same prompt and checking
how often the same twist reappears (their "Sui Generis" score, plus a
"drop ratio" for turns that occur in nearly every resample). On the
WritingPrompts dataset, human continuations of the same seed text held
a 3.7% drop ratio; GPT-4 continuations of the same seed held an 11.3%
drop ratio, roughly three times higher. In a case study, the authors
resampled a continuation of Kafka's short fragment "Give It Up" 100
times: 50 of 100 GPT-4 continuations had the policeman direct the
narrator to take the second left, 18 more had him say the second
right, and 16 mentioned a bakery. The source's own colder, more
absurdist resolution almost never appeared.

**Check:** if you regenerated this scene from the same premise several
times, would the same turn show up nearly every time? Is there a
second thread that doesn't resolve, or doesn't resolve through the
main plot? **Fix:** add a subplot that stays thematically related but
is not causally required by the main line. Let at least one thread
stay open.

### 3. Emotion shown only as physical sensation

StoryScope: "Emotional Expression to embodied" (a tightening chest,
cold sweat, a dimming room, standing in for the feeling itself)
appeared in 81% of AI stories versus 38% of human stories. The inverse
(a plain emotional label, such as "she was afraid") appeared in 29% of
human stories and only 8% of AI stories.

**Check:** read every emotional beat. Is it always rendered as a
bodily sensation or environmental mirror, never once stated directly?
**Fix:** state at least one emotion plainly somewhere in the piece.
"Show, don't tell," applied to literally every beat, is itself a tell,
not good craft.

### 4. No reference to anything real

StoryScope: human authors named a real book, film, artist, brand, or
place ("Intertextual Strategy to explicit named reference") at close
to double the AI rate, 47% versus 24%. AI stories leaned toward vague
allusion instead, 72% versus 50% for human stories.

Beguš (2024), "Experimental Narratives: A Comparison of Human
Crowdsourced Storytelling and AI Storytelling," Humanities and Social
Sciences Communications 11:1392, arXiv:2310.12902,
https://arxiv.org/abs/2310.12902, compared 250 crowdworker stories
(collected 2019) against 80 GPT-3.5/GPT-4 stories (written 2023) from
the same prompt: writing about creating and falling in love with an
artificial human. The AI stories converge on generic invented
settings. The paper quotes phrasing close to "a bustling metropolis
teeming with innovation" and "the vibrant city of Elysia" appearing
across unrelated generations, rather than a real, specific place.

**Check:** does the piece name a single real person, place, brand, or
work, or does every setting read as an invented composite? **Fix:**
name something real and specific where it would plausibly come up. A
made-up-sounding place name in an otherwise realistic story is a
signal worth removing.

### 5. Endings resolved too neatly, through the protagonist's own growth

StoryScope: "Resolution Mode to internal understanding" (the story
ends because the protagonist reaches acceptance or insight) appeared
in 47% of AI stories versus 27% of human stories. "Agency in
Resolution to protagonist choice" (the ending turns entirely on what
the protagonist decides, with no outside force) appeared in 69% of AI
stories versus 46% of human stories.

Beguš found the AI condition is "prone to wrapping up each story with
a moral lesson," and calls out phrasing close to "love knows no
boundaries" and "love transcends artificiality" as clichés that recur
in AI conclusions "as a rule," regardless of what the story was
actually about. The same comparison found darker material such as
betrayal, manipulation, and real loss thematized almost only in the
human stories; only a handful of the GPT-4 stories reached similar
depth.

**Check:** does the ending resolve because the protagonist personally
grows or accepts something? Is there a tidy moral in the last line
that would fit almost any story, not just this one? **Fix:** let an
outside event, not personal insight, force the resolution, or leave
the ending short of fully resolved. Consider letting something
genuinely bad happen and stay unrepaired.

### 6. Repeated names and stereotyped surface diversity

Beguš's comparison found heavy convergence on a small set of character
names across unrelated AI generations. In one prompt alone, GPT-3.5
named the artificial human "Ava" 10 separate times; "Victor" recurred
often enough that the paper calls it "a rather common name for the
creator"; Adam/Eve, Eliza (echoing Weizenbaum's 1960s ELIZA chatbot
and Eliza Doolittle), and Amelia (echoing Amelia Earhart) all recur as
well. Adjective choice stayed stereotyped even where the cast looked
demographically varied on the surface: female characters were
described mainly through intelligence, beauty, perfection, and grace;
male characters mainly through intelligence, perfection, and emotional
depth, with beauty and grace specifically skewed toward the female
characters. Human-written stories in the same comparison showed
noticeably higher racial diversity than the GPT-generated ones.

**Check:** would this character's name show up if you generated the
scene five more times? Do the adjectives describing each character
still sort by a stereotype once you look past who they are on paper?
**Fix:** pick a name deliberately, not a default. Check adjective
choice against the character's actual role in the plot, not their
demographic.

### 7. Character network too dense and too friendly

Nonaka and Perry (2025), "Evaluating LLM Story Generation through
Large-scale Network Analysis of Social Structures," arXiv:2510.18932,
https://arxiv.org/abs/2510.18932 (NeurIPS 2025 workshop paper), built
signed character-interaction networks (who interacts with whom, and
whether the relationship reads positive or negative) across more than
1,200 stories from four LLMs (GPT-4o, GPT-4o mini, Gemini 1.5 Pro,
Gemini 1.5 Flash) against a human corpus drawn from Project Gutenberg.
LLM-generated casts formed denser networks (0.338 to 0.470 density,
depending on model, versus 0.182 for the human stories) with
relationship sentiment skewed positive (average edge weight 0.235 to
0.659, versus -0.061, slightly negative, for the human stories). The
paper's "negative" (adversarial) sub-networks were also less dense in
LLM stories (0.222 to 0.261) than in human stories (0.313), though the
authors themselves caution that this specific result is sensitive to
named-entity-recognition artifacts and should not be over-read.

**Check:** does every character in the cast know and like the
protagonist? Does the antagonist, if any, exist in isolation, with no
allies or history of their own? **Fix:** keep some characters only
indirectly connected to each other. Let overall relationship sentiment
run neutral-to-negative rather than uniformly warm. Give an antagonist
their own real relationships.

## Pass 2: flow

### 8. The middle sags while the opening and closing are polished

Tripto, Venkatraman, Nahar, Lee (2025), "Beyond Checkmate: Exploring
the Creative Choke Points for AI Generated Texts," EMNLP 2025,
arXiv:2501.19301, https://arxiv.org/abs/2501.19301, compared human and
AI writing across news, essay, and email domains, segment by segment
(introduction, body, conclusion, framed as a chess opening,
middlegame, and endgame), across four LLMs. Once segment length is
controlled for, the body is where human and AI writing diverge most
and is the most useful segment for telling them apart, the paper's
"choke point." AI-written introductions and conclusions are harder to
tell apart from human ones (a higher false-negative rate) than the
body is. The paper also finds human writing varies its stylistic
features across the three segments noticeably more than AI writing
does; AI stays closer to one register the whole way through, including
at the start, where an unusually polished, standard-feeling opening is
itself a signal worth noticing rather than reassurance.

**Check:** read the middle third on its own. Does energy and
specificity drop compared to the opening and closing? Does the
register stay perfectly even across the whole piece? **Fix:** put the
most work into the middle section specifically. Deliberately vary
sentence length and density from section to section rather than
holding one steady rhythm.

### 9. Discourse structure follows the same template every time

Namuduri, Wu, Zheng, Wadhwa, Durrett, Li (2025), "QUDsim: Quantifying
Discourse Similarities in LLM-Generated Text," COLM 2025,
arXiv:2504.09373, https://arxiv.org/abs/2504.09373, modeled each
paragraph as answering an implicit Question Under Discussion (QUD) and
measured how often generations from the same model reuse the same
sequence of question types. Pairs of documents from the same LLM
reused discourse-move sequences at 0.80 to 1.20 average matching
two-segment templates; documents from an LLM matched against the
paper's small human comparison set at a lower but still substantial
0.30 to 0.90, depending on model pair (the study did not report a
human-to-human baseline, since its human sample was only 10
documents). The paper's own case study of a reused sequence: three
separately generated texts about a government official deciding to
conceal a secret from the public all followed the same shape, lay out
the secret, justify concealing it, describe the social consequences of
revealing it, close on the weight of responsibility now carried,
almost regardless of the specific scenario. Across the whole dataset,
Concept and Example moves were by far the most common paragraph type;
Verification and Comparison moves, a later paragraph revisiting or
challenging what an earlier one claimed, were close to absent (0.3%
and 0.2% of all moves respectively).

**Check:** list, in order, what question each paragraph or scene
answers. Is it a straight line of one thing then the next? Does
anything in the piece revisit or complicate an earlier claim? **Fix:**
if the outline is perfectly linear, reorder so at least one later
section forces a re-read of an earlier one. Add a passage that
compares or verifies something stated before, rather than only adding
new information forward.

## Pass 3: surface (do this last)

The clichés-and-vocabulary layer is real but is the layer StoryScope
found moves least on its own: a full surface-style rewrite of the AI
stories in that study took detection from 95.5% macro-F1 (AUPRC 0.996)
down to only 93.9% macro-F1 (AUPRC 0.988), a drop of 1.6 points. Use
`references/professional-docs.md`'s cross-domain checklist for the
concrete word- and sentence-level items; the same surface patterns
show up in fiction and in professional prose alike, and are catalogued
once there rather than twice.

## Self-test worth running before calling a piece finished

Borrowed directly from Xu, Jojic, Rao, Brockett, and Dolan's method
above, as a manual check rather than a resampling experiment: pick the
one plot turn you're least sure about, and ask honestly whether five
other reasonable continuations of this exact scene would land on the
same turn. If yes, it's a tell, not a choice. Change it or cut it.

## Full source list for this file

- Russell, Rajendhran, Pham, Iyyer, Wieting (2026), "StoryScope:
  Investigating idiosyncrasies in AI fiction," arXiv:2604.03136.
- Beguš (2024), "Experimental Narratives: A Comparison of Human
  Crowdsourced Storytelling and AI Storytelling," Humanities and
  Social Sciences Communications 11:1392, arXiv:2310.12902.
- Xu, Jojic, Rao, Brockett, Dolan (2025), "Echoes in AI: Quantifying
  Lack of Plot Diversity in LLM Outputs," PNAS 122 (2025),
  arXiv:2501.00273.
- Tripto, Venkatraman, Nahar, Lee (2025), "Beyond Checkmate: Exploring
  the Creative Choke Points for AI Generated Texts," EMNLP 2025,
  arXiv:2501.19301.
- Namuduri, Wu, Zheng, Wadhwa, Durrett, Li (2025), "QUDsim:
  Quantifying Discourse Similarities in LLM-Generated Text," COLM
  2025, arXiv:2504.09373.
- Nonaka, Perry (2025), "Evaluating LLM Story Generation through
  Large-scale Network Analysis of Social Structures," arXiv:2510.18932
  (NeurIPS 2025 workshop paper).

All findings above are reported as measured associations within each
study's own sample and method. None of the "fixes" listed were
themselves tested as interventions by these papers; they are this
skill's own editorial inference from what was measured, same as any
style guide built on descriptive research.
