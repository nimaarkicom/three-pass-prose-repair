# three-pass-prose-repair

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that
diagnoses and repairs writing that reads flat, generic, or obviously
AI-written, in fiction and in everyday work documents.

Most fixes for "AI-sounding" writing only swap out a few words. That barely
helps. The real problem is usually how the piece is built: a plot that
resolves too neatly, or a report that buries its point in filler. This
skill fixes that first, then the flow, then the words, in that order,
because the research it is built on found that order matters: a full
word-level rewrite moved a detector's accuracy by only 1.6 points on its
own test set, while the structural layer underneath carried the rest.

## What is in this repo

- `SKILL.md`: the skill itself. Two operations, `review` (diagnose only)
  and `repair` (fix in order), routed by text type.
- `references/`: the research the skill is built on, one file for fiction
  and narrative essays, one for everyday work documents. Every check names
  the paper it came from and the actual number that paper reported.
- `scripts/diagnose.py`: a command-line tool that reads a text file and
  scores it against five of the measurable signals the research identifies.
- `scripts/validate_frontmatter.py`: checks that `SKILL.md`'s YAML
  frontmatter actually parses. This project shipped once with an unquoted
  colon in the description field that silently broke GitHub's parser.
- `examples/`: two short fiction fixtures, one written to trip the
  diagnostic script's flags on purpose, one written not to.
- `.github/workflows/`: CI that runs both scripts above on every push.

## Using the skill

Copy this repo, or point an agent at it directly. `SKILL.md` carries its
own routing table and pass order; read it before using either operation.

```
review: diagnose only, cite the line that triggered each check, apply nothing
repair: fix architecture first, then flow, then surface word choice
```

## Using the diagnostic script

```
python3 scripts/diagnose.py path/to/draft.txt
python3 scripts/diagnose.py path/to/draft.txt --json
```

It reads a plain-text file and reports five signals: sentence-length
variance, three-item ("rule of three") sentence stacking, repeated
paragraph-opener words, a narrator directly stating a story's theme or
moral, and a short list of words measured to appear at far above human
baseline rate in LLM output. It does not call any model, does not decide
whether a text is AI-written, and is not a classifier. It flags patterns
for a human editor to check by eye, each with a real number attached. Run
it against the two files in `examples/` to see the range of output it
produces.

No dependencies beyond the Python 3 standard library. Requires Python 3.9
or later.

## Research

Every check in `references/` cites a real, published study, read directly
from its own primary source, not summarized secondhand. The two reference
files each carry a full source list at the bottom. Numbers are reported the
way the papers reported them: as measured differences within that paper's
own sample and method, not as universal rules. See `SKILL.md`'s Calibration
section before applying every check to every piece; overshooting a check as
far as possible in the opposite direction creates its own detectable
pattern.

## License

MIT, see `LICENSE`.
