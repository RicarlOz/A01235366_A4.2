"""
compute_statistics.py

Compute descriptive statistics from a file containing numeric data.

Statistics computed:
- Mean
- Median
- Mode
- Population standard deviation
- Population variance

Outputs results to the console and to a file named StatisticsResults.txt.

Constraints:
- Calculations are implemented using basic algorithms (no statistics libraries).
- Invalid data is reported and ignored; execution continues.
"""

from __future__ import annotations

import sys
import time

OUTPUT_FILENAME = "StatisticsResults.txt"


def parse_number(line: str, line_number: int) -> tuple[float | None, str | None]:
    """
    Parse a line into a float.

    Returns (value, None) for valid numbers.
    Returns (None, warning_message) for invalid/empty lines.
    """
    raw = line.strip()
    if not raw:
        return None, f"Line {line_number}: empty line ignored."

    try:
        return float(raw), None
    except ValueError:
        return None, f"Line {line_number}: invalid data '{raw}' ignored."


def mean(values: list[float]) -> float:
    """Compute the arithmetic mean."""
    total = 0.0
    for value in values:
        total += value
    return total / float(len(values))


def median(values: list[float]) -> float:
    """Compute the median."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        return sorted_vals[mid]

    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0


def mode(values: list[float]) -> float | None:
    """
    Compute the mode.

    Returns:
    - The unique mode if it exists
    - None if there is no mode or there is a tie for most frequent
    """
    counts: dict[float, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1

    max_count = 0
    for cnt in counts.values():
        max_count = max(max_count, cnt)

    if max_count <= 1:
        return None

    modes = [val for val, cnt in counts.items() if cnt == max_count]
    if len(modes) != 1:
        return None

    return modes[0]


def sqrt_newton(value: float) -> float:
    """
    Compute square root using Newton-Raphson method.

    This avoids using math.sqrt to comply with the "basic algorithms" requirement.
    """
    if value < 0.0:
        raise ValueError("Cannot compute square root of a negative number.")
    if value == 0.0:
        return 0.0

    guess = value / 2.0 if value >= 1.0 else 1.0
    for _ in range(60):
        guess = 0.5 * (guess + (value / guess))
    return guess


def variance_population(values: list[float], avg: float) -> float:
    """Compute population variance: sum((x - mean)^2) / n."""
    total = 0.0
    for value in values:
        diff = value - avg
        total += diff * diff
    return total / float(len(values))


def standard_deviation_population(values: list[float], avg: float) -> float:
    """Compute population standard deviation."""
    return sqrt_newton(variance_population(values, avg))


def format_number(value: float | None) -> str:
    """Format a number for output, or return #N/A for None."""
    if value is None:
        return "#N/A"

    text = f"{value:.10f}".rstrip("0").rstrip(".")
    return "0" if text == "-0" else text


def compute_stats(values: list[float]) -> dict[str, float | None]:
    """Compute all required descriptive statistics."""
    avg = mean(values)
    return {
        "COUNT": float(len(values)),
        "MEAN": avg,
        "MEDIAN": median(values),
        "MODE": mode(values),
        "SD": standard_deviation_population(values, avg),
        "VARIANCE": variance_population(values, avg),
    }


def build_output(stats: dict[str, float | None], elapsed: float) -> str:
    """Build the output text for console and file."""
    return (
        f"COUNT: {format_number(stats['COUNT'])}\n"
        f"MEAN: {format_number(stats['MEAN'])}\n"
        f"MEDIAN: {format_number(stats['MEDIAN'])}\n"
        f"MODE: {format_number(stats['MODE'])}\n"
        f"SD: {format_number(stats['SD'])}\n"
        f"VARIANCE: {format_number(stats['VARIANCE'])}\n"
        f"ELAPSED_SECONDS: {format_number(elapsed)}\n"
    )


def main() -> int:
    """Program entry point."""
    if len(sys.argv) < 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        return 1

    input_file = sys.argv[1]
    start = time.perf_counter()

    values: list[float] = []
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for idx, line in enumerate(file, start=1):
                value, warning = parse_number(line, idx)
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
        print("Error: No valid numeric data found in the file.")
        return 1

    stats = compute_stats(values)
    elapsed = time.perf_counter() - start
    output = build_output(stats, elapsed)

    print(output, end="")

    try:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as out:
            out.write(output)
    except OSError as exc:
        print(f"Error: could not write results file '{OUTPUT_FILENAME}': {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
