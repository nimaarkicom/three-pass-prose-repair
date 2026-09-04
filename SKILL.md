---
name: three-pass-prose-repair
description: "Fixes writing that reads flat, generic, or obviously AI-written. Most tools that try to fix this only swap out words, which barely helps. This fixes the bigger problem first: how the piece is built, then the flow, then the words last. Two modes: review (diagnose only) and repair (fix it step by step). Works on fiction and on everyday documents such as release notes, PR replies, postmortems, and technical articles."
---

# Fix writing that sounds like AI

Most tools that try to fix AI-sounding writing swap out a few words. That
barely helps. The bigger problem is usually how the piece is put together:
a story that resolves too neatly, or a report that buries its point in
filler. This skill fixes that first, before it touches a single word.

It covers two kinds of writing, because the problem shows up differently
in each:

- **Fiction and narrative essays**: a plot that resolves too cleanly,
  feelings shown only through physical sensation instead of stated
  directly, a theme the narrator states outright instead of letting the
  reader feel it.
- **Everyday documents** (release notes, PR and issue replies,
  postmortems, technical articles): filler that carries no signal, false
  neutrality where a plain judgment call was needed, the same structural
  template used for every document regardless of what it is actually for.

This is a writing-craft tool. Its goal is prose that reads like it was
built for its own situation, not formulaic, not generic, for the reader's
actual benefit. It is not a tool for beating any detector and should never
be described that way. It targets the real habits that make writing feel
thin, which happen to be the same habits the cited research measured.

## Operations

| Operation | Contract |
|---|---|
| **review** | Diagnose only. Do not edit anything. Read the routed reference file. Check the draft against each item in it. Report every match, and quote the specific line or passage that triggered it. Stop there. Apply nothing until asked. |
| **repair** | Apply fixes in order: Pass 1 architecture, Pass 2 flow, Pass 3 surface word choice. Do the passes in that order. Do not start with Pass 3; the research this skill is built on found that layer moves the least on its own. |

Both operations load the same reference material. `review` reads it as a
checklist to score against. `repair` reads it as edit instructions. For
either operation, run `scripts/diagnose.py` against the draft first (see
below) and treat its output as a starting list of passages to look at, not
a verdict.

## Routing

| Text type | Load |
|---|---|
| Fiction, short stories, narrative essays | `references/structural-tells.md` |
| Release notes, changelogs, announcements | `references/professional-docs.md`, section "Release notes and announcements" |
| PR replies, issue replies, code-review comments | `references/professional-docs.md`, section "PR and issue replies" |
| Incident postmortems, root-cause reviews | `references/professional-docs.md`, section "Postmortems and incident reviews" |
| Technical articles, deep-dive posts | `references/professional-docs.md`, section "Technical articles and deep-dive posts" |
| Any other non-fiction document | `references/professional-docs.md`, general checklist section only |

## Pass order (applies to both routes)

1. **Architecture.** For fiction: the plot's causal structure, what
   resolves and how. For a document: its argument structure, meaning what
   claims it makes, in what order, and how it resolves. Architecture comes
   first because it is the most expensive to fix after the fact, and
   word-level editing does not reach it.
2. **Flow.** Pacing, paragraph rhythm, where information is revealed
   versus withheld, whether the piece varies section to section the way a
   single author's attention naturally would, or holds one register the
   whole way through.
3. **Surface.** Clichés, repeated sentence templates, vocabulary,
   register. This is real and worth doing. It comes last, and it should
   not substitute for the first two passes.

## Diagnostic script

`scripts/diagnose.py` reads a plain-text file and flags five measurable
patterns the research in `references/` identifies. Run it before Pass 1:

```
python3 scripts/diagnose.py path/to/draft.txt
python3 scripts/diagnose.py path/to/draft.txt --json
```

It checks: sentence-length variance across the piece, three-item sentence
stacking, repeated paragraph-opening templates, a narrator stating the
piece's own theme or lesson directly, and a short list of words measured
to appear at far above human baseline rate in LLM output. It reports a
count and the flagged lines per check. It is a supporting tool, not a
replacement for the `review` operation: it counts patterns, it does not
read for meaning, and it does not decide pass or fail on its own. See its
own header comment for the exact finding each check is grounded in.

Run it against `examples/formulaic.txt` and `examples/natural.txt` to see
the range of output it produces before running it on a real draft.

## Calibration

Do not apply every check in the reference files to every piece; that just
trades one formula for another. The measured human baseline for almost
every feature below sits at a moderate value, not an extreme one.
Overshooting a check as far as possible in the opposite direction creates
its own detectable pattern. Fix what the draft actually shows, leave the
rest, and never invent a specific detail (a name, a number, a date, a
citation) to satisfy a "be more specific" check. A confident wrong detail
is worse than a plain true one.

## Research base

Every check in `references/structural-tells.md` and
`references/professional-docs.md` cites a real, published study, read
directly from its own primary source (the paper's own abstract and body
text), not summarized from another project's write-up of it. Each
reference file carries a full source list at the bottom. Numbers are
reported the way each paper reported them: as a measured difference within
that paper's own sample and method, not as a universal rule.

The anchor study for the fiction route is
[StoryScope](https://arxiv.org/abs/2604.03136) (Russell, Rajendhran, Pham,
Iyyer, Wieting, arXiv:2604.03136): 61,608 stories from human authors and
five frontier LLMs, 304 narrative-structure features, 93.2% macro-F1
human-vs-AI detection from structure alone, holding at 93.9% (down from
95.5%) after a full surface-style rewrite of the AI stories.
