"""Writes one short dad joke for make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5."""

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

MAX_CHARS = 280


def main() -> int:
    assert 1 <= len(TEXT) <= MAX_CHARS, "text must be between 1 and 280 characters"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
