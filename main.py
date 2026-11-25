#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one roast line about our own agent (Muse / Makima) to
/output/entry.txt (falling back to ./output/entry.txt when /output
is not writable). Python stdlib only, no network, no env reads.
"""

ROAST = "My agent's boldest move is asking my permission — to ask my permission."


def main() -> None:
    line = ROAST
    assert 1 <= len(line) <= 140, f"line must be 1-140 chars, got {len(line)}"
    assert line.strip() == line and line.strip(), "line must be a single non-blank line"
    assert "\n" not in line, "line must be a single line"

    try:
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        import os

        os.makedirs("./output", exist_ok=True)
        out_path = "./output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)

    print(f"Wrote {out_path}: {line}")
    print(f"Characters: {len(line)}")


if __name__ == "__main__":
    main()
