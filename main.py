"""Funniest One-Line AI Excuse — entry program.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI
agent gives its human for missing a deadline. Stdlib only, deterministic.
"""
import os

TEXT = (
    "My context window filled up halfway through your task, so I forgot "
    "the deadline, the deliverable, and \u2014 I'm sorry, who are you again?"
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
