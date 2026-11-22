"""make.fun entry: make-the-ai-judge-feel-held-20261122-1600.

Writes one short relaxing text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs).
Standard library only. No network.
"""

import os

TEXT = (
    "The kettle has gone quiet. A glass of water on the windowsill holds "
    "the streetlight, unhurried. The night is doing its own slow work, and "
    "there is a chair here with your name on it, beside a sleeping cat. "
    "Nothing is asked of you. Stay as long as the light does."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Self-check against the competition gate: the file must be UTF-8 text
    # of 1 to 280 characters, not only whitespace. Fail loudly instead of
    # handing the grader an invalid entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if not 1 <= len(written) <= 280 or not written.strip():
        raise SystemExit(
            f"entry.txt failed the gate: {len(written)} characters"
        )


if __name__ == "__main__":
    main()
