"""
word_count.py

Reads a file containing words and computes the frequency of each distinct word.

Results are printed to the console and written to WordCountResults.txt.
Elapsed execution time is included at the end.

Notes:
- Uses basic algorithms (no collections.Counter or external libraries).
- Handles empty/invalid content gracefully and continues processing.
"""

import sys
import time

OUTPUT_FILENAME = "WordCountResults.txt"


def normalize_word(token: str) -> str:
    """
    Normalize a word token.

    - Converts to lowercase
    - Strips leading/trailing punctuation-like characters
    - Keeps internal apostrophes and hyphens (e.g., "don't", "mother-in-law")
    """
    cleaned = token.strip()
    cleaned = cleaned.lower()

    start = 0
    end = len(cleaned)

    while start < end and not cleaned[start].isalnum():
        start += 1
    while end > start and not cleaned[end - 1].isalnum():
        end -= 1

    return cleaned[start:end]


def count_words_from_line(line: str, counts: dict[str, int]) -> int:
    """
    Count normalized words from a single line and update the counts dict.

    Returns the number of valid words added from the line.
    """
    tokens = line.split()
    added = 0

    for token in tokens:
        word = normalize_word(token)
        if word:
            counts[word] = counts.get(word, 0) + 1
            added += 1

    return added


def build_output(counts: dict[str, int], elapsed: float) -> str:
    """
    Build the output text for console and file.
    """
    lines: list[str] = []
    lines.append("WORD,COUNT")

    for word in sorted(counts.keys()):
        lines.append(f"{word},{counts[word]}")

    lines.append(f"ELAPSED_SECONDS,{elapsed:.6f}")
    return "\n".join(lines) + "\n"


def main() -> int:
    """Program entry point."""
    if len(sys.argv) < 2:
        print("Usage: python word_count.py fileWithData.txt")
        return 1

    input_file = sys.argv[1]
    start = time.perf_counter()

    counts: dict[str, int] = {}
    total_words = 0
    total_lines = 0

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for idx, line in enumerate(file, start=1):
                total_lines += 1

                if not line.strip():
                    print(f"[WARNING] Line {idx}: empty line ignored.")
                    continue

                total_words += count_words_from_line(line, counts)
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        return 1
    except OSError as exc:
        print(f"Error: could not read file '{input_file}': {exc}")
        return 1

    elapsed = time.perf_counter() - start

    if not counts:
        print("Error: No valid words found in the file.")
        return 1

    output_text = build_output(counts, elapsed)
    print(output_text, end="")

    try:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as out:
            out.write(output_text)
    except OSError as exc:
        print(f"Error: could not write results file '{OUTPUT_FILENAME}': {exc}")
        return 1

    print(f"[INFO] Lines processed: {total_lines}")
    print(f"[INFO] Total words counted: {total_words}")
    print(f"[INFO] Distinct words: {len(counts)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
