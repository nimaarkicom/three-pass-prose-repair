#!/usr/bin/env python3
"""diagnose.py: flag AI-writing structural and stylistic patterns in a text file.

Reads one text file and reports on five measurable signals drawn from the
research in references/. It does not call any model and does not decide
whether a text is AI-written. It flags patterns a human editor can check by
eye, with a number attached to each one.

Signals:
  1. Sentence-length variance ("burstiness"). Low variance across a
     document is associated with AI writing (Tripto et al. 2025).
  2. Rule-of-three stacking. A sentence built from three parallel items
     or clauses, joined by commas and a final "and"/"or". Overused, this
     is one of the structural tells Russell et al. 2025 found survives
     even an AI paraphrase pass.
  3. Repeated paragraph-opener templates. Consecutive or frequent reuse
     of the same opening word or two across paragraphs, one shape of the
     "discourse template" pattern QUDsim (Namuduri et al. 2025) measured.
  4. Self-explaining theme / moralizing language. A crude keyword and
     pattern match for a narrator or writer stating the point instead of
     showing it (StoryScope's "Narratorial Thematic Commentary", Beguš's
     moralizing endings).
  5. Overused vocabulary. A short word list Reinhart et al. 2025 found
     LLMs use at far above human baseline frequency.

Usage:
    python3 diagnose.py FILE [--json]

Exit code is always 0 on a successful run. A missing or unreadable file
exits 1.
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

# --- Text splitting -------------------------------------------------------

SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")


def split_paragraphs(text):
    parts = re.split(r"\n\s*\n", text.strip())
    return [p.strip() for p in parts if p.strip()]


def split_sentences(paragraph):
    flat = re.sub(r"\s+", " ", paragraph.strip())
    if not flat:
        return []
    pieces = SENTENCE_END_RE.split(flat)
    return [p.strip() for p in pieces if p.strip()]


def word_count(sentence):
    return len(re.findall(r"[A-Za-z0-9']+", sentence))


# --- Signal 1: sentence-length variance -----------------------------------

def sentence_length_signal(sentences):
    lengths = [word_count(s) for s in sentences if word_count(s) > 0]
    if len(lengths) < 4:
        return {
            "sentence_count": len(lengths),
            "mean_length": None,
            "stdev_length": None,
            "coefficient_of_variation": None,
            "flag": False,
            "note": "too few sentences to score (need at least 4)",
        }
    mean = statistics.mean(lengths)
    stdev = statistics.stdev(lengths)
    cv = stdev / mean if mean else 0.0
    # Human prose in the studied corpora typically shows CV well above 0.4.
    # A document that stays this uniform sentence to sentence is flagged.
    flag = cv < 0.35
    return {
        "sentence_count": len(lengths),
        "mean_length": round(mean, 2),
        "stdev_length": round(stdev, 2),
        "coefficient_of_variation": round(cv, 3),
        "flag": flag,
        "note": "low variance in sentence length (uniform pacing)" if flag else "normal variance",
    }


# --- Signal 2: rule-of-three stacking --------------------------------------

# A parallel triad: three comma-separated spans, the last introduced by
# "and" or "or", each span short enough to read as a listed item rather
# than an unrelated long clause.
RULE_OF_THREE_RE = re.compile(
    r"\b([\w'-]+(?:\s[\w'-]+){0,4}),\s([\w'-]+(?:\s[\w'-]+){0,4}),\s(?:and|or)\s([\w'-]+(?:\s[\w'-]+){0,4})\b"
)


def rule_of_three_signal(sentences):
    hits = []
    for s in sentences:
        for m in RULE_OF_THREE_RE.finditer(s):
            hits.append(m.group(0))
    ratio = len(hits) / len(sentences) if sentences else 0.0
    flag = ratio > 0.12
    return {
        "sentence_count": len(sentences),
        "triad_count": len(hits),
        "triad_ratio": round(ratio, 3),
        "examples": hits[:5],
        "flag": flag,
        "note": "frequent three-item stacking" if flag else "not frequent",
    }


# --- Signal 3: repeated paragraph openers ----------------------------------

def paragraph_opener_signal(paragraphs):
    openers = []
    for p in paragraphs:
        words = re.findall(r"[A-Za-z0-9']+", p)
        openers.append(" ".join(w.lower() for w in words[:2]))
    if len(openers) < 3:
        return {
            "paragraph_count": len(paragraphs),
            "distinct_openers": len(set(openers)),
            "repeat_ratio": None,
            "flag": False,
            "note": "too few paragraphs to score (need at least 3)",
        }
    counts = {}
    for o in openers:
        if not o:
            continue
        counts[o] = counts.get(o, 0) + 1
    repeated = sum(c for c in counts.values() if c > 1)
    repeat_ratio = repeated / len(openers) if openers else 0.0
    flag = repeat_ratio > 0.3
    top = sorted(counts.items(), key=lambda kv: -kv[1])[:5]
    return {
        "paragraph_count": len(paragraphs),
        "distinct_openers": len(counts),
        "repeat_ratio": round(repeat_ratio, 3),
        "top_openers": top,
        "flag": flag,
        "note": "paragraphs reuse the same opening words often" if flag else "openers vary",
    }


# --- Signal 4: self-explaining theme / moralizing --------------------------

THEME_PATTERNS = [
    r"\bthe (moral|lesson|point) (of (the|this) story )?(is|was)\b",
    r"\bthis taught (me|us|him|her|them)\b",
    r"\b(and|so) (I|we) (finally )?(realized|understood|learned) that\b",
    r"\bin the end,? (I|we|he|she|they) (realized|understood|learned)\b",
    r"\b(love|hope|courage|friendship) (knows no|transcends|conquers)\b",
    r"\bwhat (this|it) (really )?(means|meant) (is|was)\b",
    r"\bthe truth (is|was) that\b",
    r"\bif (there('s| is)|there was) one thing (I|we) (learned|knew)\b",
]
THEME_RE = re.compile("|".join(THEME_PATTERNS), re.IGNORECASE)


def theme_statement_signal(sentences):
    hits = [s for s in sentences if THEME_RE.search(s)]
    ratio = len(hits) / len(sentences) if sentences else 0.0
    flag = len(hits) > 0
    return {
        "sentence_count": len(sentences),
        "theme_statement_count": len(hits),
        "ratio": round(ratio, 3),
        "examples": hits[:5],
        "flag": flag,
        "note": "narrator states the theme/moral directly" if flag else "no direct theme statement found",
    }


# --- Signal 5: overused vocabulary -----------------------------------------

OVERUSED_WORDS = [
    "tapestry", "camaraderie", "intricate", "underscore", "underscores",
    "underscored", "unspoken", "amidst", "palpable", "solace", "testament",
    "bustling", "vibrant", "nestled", "boundless", "ever-evolving",
    "in today's fast-paced world", "in the world of", "delve", "delving",
]


def overused_vocabulary_signal(text):
    lower = text.lower()
    total_words = max(len(re.findall(r"[A-Za-z0-9']+", text)), 1)
    found = {}
    for w in OVERUSED_WORDS:
        n = len(re.findall(r"\b" + re.escape(w) + r"\b", lower))
        if n:
            found[w] = n
    total_hits = sum(found.values())
    rate_per_1000 = total_hits / total_words * 1000
    flag = rate_per_1000 > 1.0
    return {
        "word_count": total_words,
        "hits": found,
        "total_hits": total_hits,
        "rate_per_1000_words": round(rate_per_1000, 3),
        "flag": flag,
        "note": "flagged vocabulary appears above baseline rate" if flag else "flagged vocabulary rare or absent",
    }


# --- Report -----------------------------------------------------------------

def diagnose(text):
    paragraphs = split_paragraphs(text)
    sentences = [s for p in paragraphs for s in split_sentences(p)]
    signals = {
        "sentence_length_variance": sentence_length_signal(sentences),
        "rule_of_three_stacking": rule_of_three_signal(sentences),
        "repeated_paragraph_openers": paragraph_opener_signal(paragraphs),
        "theme_stated_directly": theme_statement_signal(sentences),
        "overused_vocabulary": overused_vocabulary_signal(text),
    }
    flagged = [name for name, sig in signals.items() if sig.get("flag")]
    return {
        "paragraph_count": len(paragraphs),
        "sentence_count": len(sentences),
        "signals": signals,
        "flagged_signal_count": len(flagged),
        "flagged_signals": flagged,
    }


def format_text_report(path, report):
    lines = []
    lines.append(f"three-pass-prose-repair diagnostic: {path}")
    lines.append(f"paragraphs: {report['paragraph_count']}  sentences: {report['sentence_count']}")
    lines.append(f"flagged signals: {report['flagged_signal_count']} / {len(report['signals'])}")
    lines.append("")
    for name, sig in report["signals"].items():
        mark = "FLAG" if sig.get("flag") else "ok"
        lines.append(f"[{mark}] {name}")
        lines.append(f"    {sig.get('note', '')}")
        for key, value in sig.items():
            if key in ("flag", "note"):
                continue
            lines.append(f"    {key}: {value}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Flag AI-writing structural patterns in a text file.")
    parser.add_argument("file", help="path to a plain-text file")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON instead of a text report")
    args = parser.parse_args()

    path = Path(args.file)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot read {path}: {exc}", file=sys.stderr)
        return 1

    report = diagnose(text)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(format_text_report(str(path), report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
