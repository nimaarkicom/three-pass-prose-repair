# three-pass-prose-repair

A Claude Agent Skill that fixes writing that reads flat, generic, or
obviously AI-written.

Most tools that try to fix AI-sounding writing only swap out a few
words. That barely helps. The real problem is usually how the piece is
built: a plot that resolves too neatly, or a document that buries its
point in filler. This skill fixes that first, before it touches a
single word.

## What is in this repo

- `SKILL.md`: the skill itself. Two operations, `review` (diagnose
  only) and `repair` (fix in order: architecture, then flow, then
  surface word choice). Routes fiction to one reference file and
  professional documents (release notes, PR replies, postmortems,
  technical articles) to another.
- `references/`: the research behind every check the skill runs.
  Built from primary sources: real papers, fetched and read directly,
  not summarized secondhand. Every claim carries its own citation and
  its own number.
- `scripts/diagnose.py`: a command-line tool that reads a text file
  and scores it against five of the measurable signals from
  `references/`. It does not call a model and does not decide whether
  a text is AI-written; it counts real, checkable patterns.
- `examples/`: two short fixtures, one written to be formulaic, one
  written to vary naturally, used to prove the script actually tells
  them apart.
- `.github/workflows/`: CI that validates `SKILL.md`'s YAML
  frontmatter and re-runs the diagnostic script against both fixtures
  on every push.

## Using the script

```
python3 scripts/diagnose.py path/to/draft.txt
python3 scripts/diagnose.py path/to/draft.txt --json
```

No dependencies beyond the Python 3 standard library.

## Using the skill

Point a Claude Agent Skills-compatible tool at this repo, or copy
`SKILL.md` and `references/` into a skills directory. `SKILL.md`
covers routing and the operation contract.

## License

MIT. See `LICENSE`.
