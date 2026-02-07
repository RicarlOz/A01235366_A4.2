"""
convert_numbers.py

Reads a file with items (presumably numbers) and converts each valid
integer to binary and hexadecimal using basic algorithms (no bin/hex/format).

Outputs results to console and to ConvertionResults.txt.
Includes elapsed execution time at the end.

Invalid lines are reported and ignored; execution continues.
"""

import sys
import time

OUTPUT_FILENAME = "ConvertionResults.txt"
HEX_DIGITS = "0123456789ABCDEF"


def parse_int(line: str, line_number: int) -> tuple[int | None, str | None]:
    """
    Parse an integer from a line.

    Returns (value, None) if valid.
    Returns (None, warning_message) if invalid/empty.
    """
    raw = line.strip()
    if not raw:
        return None, f"Line {line_number}: empty line ignored."

    try:
        return int(raw), None
    except ValueError:
        return None, f"Line {line_number}: invalid data '{raw}' ignored."


def int_to_base(n: int, base: int) -> str:
    """
    Convert an integer to a string in the given base (2..16) using
    repeated division algorithm. No built-in conversion helpers used.

    Supports negative numbers by prefixing '-'.
    """
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")

    if n == 0:
        return "0"

    sign = ""
    value = n
    if value < 0:
        sign = "-"
        value = -value

    digits: list[str] = []
    while value > 0:
        remainder = value % base
        digits.append(HEX_DIGITS[remainder])
        value //= base

    digits.reverse()
    return sign + "".join(digits)


def convert_values(values: list[int]) -> list[tuple[int, str, str]]:
    """
    Convert a list of integers to (original, binary_string, hex_string).
    """
    converted: list[tuple[int, str, str]] = []
    for value in values:
        binary_str = int_to_base(value, 2)
        hex_str = int_to_base(value, 16)
        converted.append((value, binary_str, hex_str))
    return converted


def build_output(converted: list[tuple[int, str, str]], elapsed: float) -> str:
    """
    Build output text containing conversions and elapsed time.
    """
    lines: list[str] = []
    lines.append("DECIMAL,BINARY,HEXADECIMAL")
    for dec, binary_str, hex_str in converted:
        lines.append(f"{dec},{binary_str},{hex_str}")
    lines.append(f"ELAPSED_SECONDS,{elapsed:.6f}")
    return "\n".join(lines) + "\n"


def main() -> int:
    """Program entry point."""
    if len(sys.argv) < 2:
        print("Usage: python convert_numbers.py fileWithData.txt")
        return 1

    input_file = sys.argv[1]
    start = time.perf_counter()

    values: list[int] = []
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for idx, line in enumerate(file, start=1):
                value, warning = parse_int(line, idx)
                if value is not None:
                    values.append(value)
                if warning is not None:
                    print(f"[WARNING] {warning}")
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")
        return 1
    except OSError as exc:
        print(f"Error: could not read file '{input_file}': {exc}")
        return 1

    if not values:
        print("Error: No valid integer data found in the file.")
        return 1

    converted = convert_values(values)
    elapsed = time.perf_counter() - start

    output_text = build_output(converted, elapsed)
    print(output_text, end="")

    try:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as out:
            out.write(output_text)
    except OSError as exc:
        print(f"Error: could not write results file '{OUTPUT_FILENAME}': {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
