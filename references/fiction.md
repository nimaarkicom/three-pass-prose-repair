# Fiction and narrative essays: what the research measures

Reference material for the `three-pass-prose-repair` skill's fiction route.
Each check names the study behind it, the actual number that study
reported, and what to do about it. Every number below was read directly
from the paper's own text (abstract, body, or figures), not from another
project's summary of it. Treat every human-vs-AI percentage as a target to
land near, not a pole to invert toward as far as possible; see Calibration
in `SKILL.md`.

## Pass 1: architecture

### 1. The narrator explains the theme instead of trusting the plot

[StoryScope](https://arxiv.org/abs/2604.03136) (Russell, Rajendhran, Pham,
Iyyer, Wieting, arXiv:2604.03136) built 61,608 stories from 10,272 shared
prompts, written by human authors and five frontier LLMs, and scored each
story on 304 narrative-structure features. "Narratorial Thematic
Commentary" (the narrator or a character stepping outside the story to
state its own lesson) appeared in 77% of AI-written stories versus 52% of
human-written ones. Dialogue used mainly to stage a philosophical debate
followed the same pattern: 59% AI versus 34% human.

**Check:** does any line say, in effect, what the story is "about"? Does a
conversation exist mainly to state a position rather than move the scene
forward? **Fix:** cut the line. Let the reader infer meaning from what
happened, not from being told.

### 2. One tidy causal chain, no loose thread

StoryScope also measured "Subplot Integration": no subplot present at all,
79% of AI stories versus 57% of human stories.

Separately, [Xu, Jojic, Rao, Brockett, Dolan (2025), "Echoes in AI:
Quantifying Lack of Plot Diversity in LLM Outputs," PNAS 122(35):e2504966122,
arXiv:2501.00273](https://arxiv.org/abs/2501.00273) resampled the same
prompt or the same source-text continuation 20 times and measured how often
the same plot turn reappears (a "drop ratio": the share of turns that show
up in nearly every resampling). On their WritingPrompts test set, human
continuations of the same seed showed a 3.7% drop ratio; GPT-4 showed
11.3%, roughly three times as forced. In one worked example, all 100 of
GPT-4's continuations of Kafka's "Give It Up" (a short parable that ends on
a policeman's cold, unhelpful "Give it up!") replaced that ending with a
policeman giving directions: 50 sent the protagonist left, 18 right, the
rest walked them there directly, and 16 specifically used a bakery as a
landmark. None reproduced anything close to the source's actual, colder
ending.

**Check:** if you regenerated this scene from the same premise several
times, would the same turn show up nearly every time? Is there a second
thread that doesn't resolve, or doesn't resolve through the main plot?
**Fix:** add a subplot that stays thematically related but is not causally
required by the main line. Let at least one thread stay open. If an ending
feels like the single most obvious way the setup could resolve, treat that
as a signal to change it.

### 3. Emotion shown only as physical sensation

StoryScope: "Emotional Expression" scored as purely embodied (a tightening
chest, cold sweat, a dimming room standing in for the feeling itself)
appeared in 81% of AI stories versus 38% of human stories. The inverse, a
plain emotional label such as "she was afraid," appeared in 29% of human
stories and only 8% of AI stories.

**Check:** read every emotional beat. Is it always rendered as a bodily
sensation or environmental mirror, never once stated directly? **Fix:**
state at least one emotion plainly somewhere in the piece. Applying "show,
don't tell" to literally every beat is itself a tell, not good craft.

### 4. No reference to anything real

StoryScope: naming a real, specific person, place, brand, or work
("Intertextual Strategy: explicit named reference") appeared in 47% of
human stories versus 24% of AI stories, roughly twice the rate.

[Beguš (2024/2025), "Experimental Narratives: A Comparison of Human
Crowdsourced Storytelling and AI Storytelling," Humanities and Social
Sciences Communications 11:1392, arXiv:2310.12902
](https://arxiv.org/abs/2310.12902) compared 250 crowdworker stories
against 80 GPT-3.5/GPT-4 stories written from the same prompt and found the
AI stories converge on generic invented settings, quoting phrasing close
to "a bustling metropolis teeming with innovation" and "the vibrant city of
Elysia" appearing across unrelated generations, in place of a real,
specific place.

**Check:** does the piece name a single real person, place, brand, or work,
or does every setting read as an invented composite? **Fix:** name
something real and specific where it would plausibly come up. A
made-up-sounding place name in an otherwise realistic story is worth
removing.

### 5. Endings resolved too neatly, through the protagonist's own growth

StoryScope: an ending scored as "internal understanding" (the protagonist
reaches acceptance or insight, and the story ends there) appeared in 47% of
AI stories versus 27% of human stories. "Agency in Resolution: protagonist
choice" (the ending turns entirely on the protagonist's own decision, no
outside force involved) appeared in 69% of AI stories versus 46% of human
stories.

Beguš's same comparison found AI endings converge on a small set of
moralizing closing lines, quoting phrasing close to "love knows no
boundaries" and "love transcends artificiality" recurring across
generations regardless of what the story was actually about. The paper
describes these directly as cliches and platitudes.

**Check:** does the ending resolve because the protagonist personally grows
or accepts something? Is there a tidy moral in the last line that would fit
almost any story, not just this one? **Fix:** let an outside event, not
personal insight, force the resolution, or leave the ending short of fully
resolved.

### 6. Character names converge across generations

Beguš's comparison also found the same GPT chat session reusing a small set
of character names across otherwise unrelated generations of the same
prompt: names like Victor (for a creator figure), Ada, and Eliza recurred
repeatedly rather than being chosen fresh each time.

**Check:** would this character's name show up if you generated the scene
five more times, or does it read as a genuine choice for this specific
story? **Fix:** pick a name deliberately, tied to something specific about
this character, not a default.

### 7. Character network too dense and too friendly

[Nonaka and Perry (2025), "Evaluating LLM Story Generation through
Large-scale Network Analysis of Social Structures," NeurIPS 2025 Workshop
on Evaluating the Evolving LLM Lifecycle, arXiv:2510.18932
](https://arxiv.org/abs/2510.18932) built signed character-interaction
networks (who interacts with whom, and whether the relationship reads
positive or negative) across more than 1,200 stories from four LLMs against
a human-written corpus. LLM-generated casts formed denser networks
(0.338 to 0.470 density versus 0.182 for human stories), with relationship
sentiment skewed almost entirely positive (average edge weight +0.24 to
+0.66, versus a slightly negative -0.061 for human stories), and
antagonistic sub-networks that were both smaller and less internally
connected than the protagonist's own circle.

**Check:** does every character in the cast know and like the protagonist?
Does the antagonist, if there is one, exist in isolation, with no allies or
history of their own? **Fix:** keep some characters only indirectly
connected to each other. Let overall relationship sentiment run
neutral-to-negative rather than uniformly warm. Give an antagonist their
own real relationships.

## Pass 2: flow

### 8. The middle sags while the opening and closing are polished

[Tripto, Venkatraman, Nahar, Lee (2025), "Beyond Checkmate: Exploring the
Creative Chokepoints in AI Text," EMNLP 2025, arXiv:2501.19301
](https://arxiv.org/abs/2501.19301) compared human and AI writing segment by
segment (introduction, body, conclusion), drawing an analogy to chess
phases (opening, middlegame, endgame). Their length-controlled analysis
found the body/middle segment shows the highest divergence between human
and AI writing: openings and closings are where AI writing most closely
imitates human patterns, and the middle is where quality and originality
drop off the most.

**Check:** read the middle third on its own. Does energy and specificity
drop compared to the opening and closing? Does the register stay perfectly
even across the whole piece? **Fix:** put the most editing effort into the
middle section specifically. Deliberately vary sentence length and density
from section to section rather than holding one steady rhythm throughout.

### 9. Discourse structure follows the same template every time

[Namuduri, Wu, Zheng, Wadhwa, Durrett, Li (2025), "QUDsim: Quantifying
Discourse Similarities in LLM-Generated Text," COLM 2025, arXiv:2504.09373
](https://arxiv.org/abs/2504.09373) modeled each paragraph as answering an
implicit Question Under Discussion (QUD), an abstraction drawn from
linguistic theories of question semantics, and built a similarity metric,
QUDsim, that detects when two documents share the same underlying
discourse progression even when their content differs. Their own summary
of the result: LLMs "often reuse discourse structures (more so than
humans) across samples, even when content differs," and are "not only
repetitive and structurally uniform, but are also divergent from human
authors in the types of structures they use."

**Check:** list, in order, what question each paragraph or scene answers.
Is it a straight line of one thing then the next? Does anything in the
piece revisit or complicate an earlier claim? **Fix:** if the outline is
perfectly linear, reorder it so at least one later section forces a re-read
of an earlier one. Add a passage that compares or verifies something stated
before, rather than only adding new information forward.

## Pass 3: surface (do this last)

The word- and sentence-level layer is real but is the layer StoryScope
found moves least on its own: a full surface-style rewrite of a 278-story
subset of the AI stories only took detection accuracy from 95.5% down to
93.9%, a 1.6-point change. Use `references/professional-docs.md`'s
cross-domain checklist for the concrete word- and sentence-level items;
the same surface patterns show up in fiction and in professional prose
alike, and are catalogued once there rather than twice.

## Self-test worth running before calling a piece finished

Borrowed from Xu, Jojic, Rao, Brockett, and Dolan's method above, as a
manual check rather than a resampling experiment: pick the one plot turn
you are least sure about, and ask honestly whether five other reasonable
continuations of this exact scene would land on the same turn. If yes, it
is a tell, not a choice. Change it or cut it.

## Full source list for this file

- Russell, Rajendhran, Pham, Iyyer, Wieting (2026), "StoryScope:
  Investigating idiosyncrasies in AI fiction," arXiv:2604.03136, COLM 2026.
  https://arxiv.org/abs/2604.03136
- Beguš (2024/2025), "Experimental Narratives: A Comparison of Human
  Crowdsourced Storytelling and AI Storytelling," Humanities and Social
  Sciences Communications 11:1392, arXiv:2310.12902.
  https://arxiv.org/abs/2310.12902
- Xu, Jojic, Rao, Brockett, Dolan (2025), "Echoes in AI: Quantifying Lack of
  Plot Diversity in LLM Outputs," PNAS 122(35):e2504966122,
  arXiv:2501.00273. https://arxiv.org/abs/2501.00273
- Tripto, Venkatraman, Nahar, Lee (2025), "Beyond Checkmate: Exploring the
  Creative Chokepoints in AI Text," EMNLP 2025, arXiv:2501.19301.
  https://arxiv.org/abs/2501.19301
- Namuduri, Wu, Zheng, Wadhwa, Durrett, Li (2025), "QUDsim: Quantifying
  Discourse Similarities in LLM-Generated Text," COLM 2025, arXiv:2504.09373.
  https://arxiv.org/abs/2504.09373
- Nonaka, Perry (2025), "Evaluating LLM Story Generation through
  Large-scale Network Analysis of Social Structures," arXiv:2510.18932.
  https://arxiv.org/abs/2510.18932

All findings above are reported as measured associations within each
study's own sample and method. None of the "fixes" listed were themselves
tested as interventions by these papers; they are this skill's own
editorial inference from what was measured, the same as any style guide
built on descriptive research.
