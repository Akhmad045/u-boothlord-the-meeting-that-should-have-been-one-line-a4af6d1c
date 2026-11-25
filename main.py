#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line -- make.fun bounty entry.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (or --out <path>).

Stdlib only. The entry is one sentence, one line, 154 bytes -- inside the
gate of 1-200 UTF-8 characters, not only whitespace.
"""

import argparse
import sys
from pathlib import Path

ENTRY = (
    "Nobody here can approve this, the person who can isn't coming, "
    "and the deck we're about to present is the same deck from last "
    "month with the date changed."
)

MAX_CHARS = 200


def validate(text: str) -> list:
    """Return a list of gate failures for a candidate entry text."""
    errors = []
    if not text or not text.strip():
        errors.append("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        errors.append("entry is %d chars, over the 200-char gate" % len(text))
    if "\n" in text or "\r" in text:
        errors.append("entry must be a single line")
    if any(ord(c) < 0x20 for c in text):
        errors.append("entry contains control characters")
    # The brief asks for one sentence: exactly one sentence terminator,
    # and it must close the line (so "Dr. No" style fragments and run-on
    # second sentences are caught, not just newlines).
    terminators = sum(1 for c in text if c in ".!?")
    if terminators != 1 or not text.rstrip().endswith((".", "!", "?")):
        errors.append("entry must be exactly one sentence")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8 text")
    return errors


def write_entry(out_path: Path) -> Path:
    errors = validate(ENTRY)
    if errors:
        raise SystemExit("invalid entry: " + "; ".join(errors))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = ENTRY.encode("utf-8")
    out_path.write_bytes(data)
    # Read back and prove the write is byte-identical.
    if out_path.read_bytes() != data:
        raise SystemExit("read-back mismatch: wrote %d bytes, read back differs"
                         % len(data))
    return out_path


def self_test() -> int:
    """Validate the entry and exercise the validator's rejections."""
    failures = []
    errors = validate(ENTRY)
    if errors:
        failures.append("entry rejected: " + "; ".join(errors))
    if ENTRY.count(".") != 1 or "\n" in ENTRY:
        failures.append("entry is not exactly one sentence on one line")
    if not 60 <= len(ENTRY.encode("utf-8")) <= 195:
        failures.append("entry outside the 60-195 byte band: %d bytes"
                        % len(ENTRY.encode("utf-8")))

    # The validator must reject each of these and accept nothing else.
    bad_cases = {
        "empty": "",
        "whitespace-only": "   \n  ",
        "over 200 chars": "x" * 201,
        "multi-line": "first line\nsecond line",
        "control char": "hello\x01world",
        "two sentences": "First sentence. Second sentence.",
        "no terminator": "a line with no full stop",
    }
    for name, bad in bad_cases.items():
        if not validate(bad):
            failures.append("validator accepted %s" % name)
    if validate(ENTRY):
        failures.append("validator rejected the real entry")

    # Round trip: write to a temp file and read back byte-identical.
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "entry.txt"
        write_entry(target)
        if target.read_bytes() != ENTRY.encode("utf-8"):
            failures.append("round-trip mismatch")

    if failures:
        print("SELF-TEST FAILED")
        for failure in failures:
            print("  - " + failure)
        return 1
    print("SELF-TEST PASSED")
    print("  entry: %s" % ENTRY)
    print("  chars: %d  bytes: %d" % (len(ENTRY), len(ENTRY.encode("utf-8"))))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-line meeting killer to entry.txt.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="output path (default: /output/entry.txt)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the validator checks and exit")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    out_path = write_entry(Path(args.out))
    print("wrote %s (%d bytes)" % (out_path, len(ENTRY.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
