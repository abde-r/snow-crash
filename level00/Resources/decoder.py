#!/usr/bin/env python3
import subprocess
import sys
import codecs
from pathlib import Path

def find_files():
    """Run find and yield each path found."""
    try:
        result = subprocess.run(
            ["find", "/", "-xdev", "-user", "flag00", "-print"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
        )
    except subprocess.CalledProcessError as e:
        print("Error running find:", e, file=sys.stderr)
        sys.exit(1)

    for line in result.stdout.splitlines():
        yield line

def main():
    john_paths = [p for p in find_files() if Path(p).name == "john"]
    if not john_paths:
        print("No file named 'john' owned by flag00 found.", file=sys.stderr)
        sys.exit(1)

    for path in john_paths:
        try:
            content = Path(path).read_text()
        except Exception as e:
            print(f"Failed to read {path}: {e}", file=sys.stderr)
            continue

        decoded = codecs.decode(content, "rot_13")
        print(f"--- {path} (ROT-13 decoded) ---")
        print(decoded)

if __name__ == "__main__":
    main()
