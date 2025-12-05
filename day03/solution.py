import argparse
from pathlib import Path
from typing import TextIO


def largest_joltage(batteries: str) -> int:
    first = 0
    second = 0
    for i in range(len(batteries) - 1):
        if int(batteries[i]) > first:
            first = int(batteries[i])
            second = 0
        if int(batteries[i + 1]) > second:
            second = int(batteries[i + 1])
    return int(f"{first}{second}")


def total_joltage(banks: list[str]) -> int:
    return sum([largest_joltage(batteries) for batteries in banks])


def parse_banks(banks_input: TextIO) -> list[str]:
    return [l.strip() for l in banks_input]


def main(input_path: Path):
    with open(input_path, "r") as f:
        banks = parse_banks(f)
    print(total_joltage(banks))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
