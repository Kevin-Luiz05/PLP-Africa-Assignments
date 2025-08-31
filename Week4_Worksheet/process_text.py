#!/usr/bin/env python3
"""
PLP Africa – Week 4 Day 2
File Handling + Exception Handling Assignment

Features:
- Asks the user for an input filename (handles errors if not found or unreadable).
- Lets the user choose one or more text transformations (pure Python, no external libs).
- Writes a modified version to a new output file in the same folder.
- Prints a summary and where to find the output file.
"""

from pathlib import Path
import sys
import re
from datetime import datetime


def read_text_file(path: Path, encoding: str = "utf-8") -> str:
    """Read the entire file and return its content as a string."""
    try:
        with path.open("r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        raise
    except PermissionError:
        print(f"[ERROR] Permission denied when reading: {path}")
        raise
    except IsADirectoryError:
        print(f"[ERROR] That path is a directory, not a file: {path}")
        raise
    except UnicodeDecodeError:
        print(f"[ERROR] Could not decode file with {encoding}. Try a different encoding (e.g., 'utf-8-sig').")
        raise


def write_text_file(path: Path, content: str, encoding: str = "utf-8") -> None:
    """Write content to the given path. Creates/overwrites the file."""
    try:
        with path.open("w", encoding=encoding, newline="\n") as f:
            f.write(content)
    except PermissionError:
        print(f"[ERROR] Permission denied when writing: {path}")
        raise
    except IsADirectoryError:
        print(f"[ERROR] Output path is a directory, not a file: {path}")
        raise


def transform_upper(text: str) -> str:
    return text.upper()


def transform_lower(text: str) -> str:
    return text.lower()


def transform_title(text: str) -> str:
    return text.title()


def transform_line_numbers(text: str) -> str:
    lines = text.splitlines()
    # Width aligns numbers nicely (e.g., 3 digits)
    width = max(2, len(str(len(lines))))
    numbered = [f"{str(i+1).rjust(width)} | {line}" for i, line in enumerate(lines)]
    return "\n".join(numbered)


def transform_trim_trailing_spaces(text: str) -> str:
    # Remove trailing spaces from each line
    return "\n".join(line.rstrip() for line in text.splitlines())


def transform_collapse_blank_lines(text: str) -> str:
    # Replace runs of 2+ blank lines with a single blank line
    return re.sub(r"\n{3,}", "\n\n", text)


def transform_tabs_to_spaces(text: str, spaces: int = 4) -> str:
    return text.expandtabs(spaces)


def get_menu() -> str:
    return (
        "\nChoose one or more transformations (comma-separated):\n"
        "  1) UPPERCASE\n"
        "  2) lowercase\n"
        "  3) Title Case\n"
        "  4) Add line numbers\n"
        "  5) Trim trailing spaces\n"
        "  6) Collapse extra blank lines\n"
        "  7) Replace tabs with 4 spaces\n"
        "Example: 1,4,5\n"
    )


def apply_transformations(text: str, choices: list[str]) -> str:
    """Apply selected transformations in the order chosen."""
    for c in choices:
        c = c.strip()
        if c == "1":
            text = transform_upper(text)
        elif c == "2":
            text = transform_lower(text)
        elif c == "3":
            text = transform_title(text)
        elif c == "4":
            text = transform_line_numbers(text)
        elif c == "5":
            text = transform_trim_trailing_spaces(text)
        elif c == "6":
            text = transform_collapse_blank_lines(text)
        elif c == "7":
            text = transform_tabs_to_spaces(text, spaces=4)
        else:
            print(f"[WARN] Ignoring unknown option: {c}")
    return text


def suggest_output_name(input_path: Path, suffix: str = "processed") -> Path:
    # E.g., input: notes.txt -> notes.processed.txt
    return input_path.with_name(f"{input_path.stem}.{suffix}{input_path.suffix or '.txt'}")


def main():
    print("=== PLP Africa – File Read & Write + Exception Handling ===")

    # Ask user for filename (relative or absolute)
    raw = input("Enter path to the input text file (e.g., sample_input.txt): ").strip().strip('"')
    input_path = Path(raw).expanduser()

    # Optional: ask encoding if you like. We'll default to utf-8.
    encoding = "utf-8"

    # Read the file (with robust error handling)
    try:
        original = read_text_file(input_path, encoding=encoding)
    except Exception:
        # Already printed a useful message; stop gracefully
        sys.exit(1)

    print(get_menu())
    choices_raw = input("Your choice(s): ").strip()
    choices = [c.strip() for c in choices_raw.split(",")] if choices_raw else []

    processed = apply_transformations(original, choices)

    # Add a header/footer stamp to stand out (optional, makes it “unique”)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"--- Processed on {timestamp} | Source: {input_path.name} ---\n"
    footer = f"\n--- End of processed file ---\n"
    processed = header + processed + footer

    output_path = suggest_output_name(input_path)
    try:
        write_text_file(output_path, processed, encoding=encoding)
    except Exception:
        sys.exit(1)

    # Summary
    print("\n✅ Success!")
    print(f"Input : {input_path.resolve()}")
    print(f"Output: {output_path.resolve()}")
    print("Tip: Open the output file to verify transformations.\n")


if __name__ == "__main__":
    main()
