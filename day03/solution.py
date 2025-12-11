import argparse
from functools import reduce
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


def max_at(batteries: list[int]) -> tuple[int, int]:
    index = -1
    max = 0
    for i, n in enumerate(batteries):
        if n > max:
            max = n
            index = i
    return max, index


def largest_joltage_override(batteries: str) -> int:
    numbers = [int(n) for n in batteries]
    digits = largest_digit(numbers, [], 12)
    return reduce(lambda x, y: x * 10 + y, digits)


def largest_digit(numbers: list[int], current, left) -> list[int]:
    if left == 0:
        return current
    usable = numbers[:-(left - 1)] if left > 1 else numbers
    max, index = max_at(usable)
    return largest_digit(numbers[index + 1 :], current + [max], left - 1)


def total_joltage(banks: list[str], part: int = 1) -> int:
    joltage = largest_joltage if part == 1 else largest_joltage_override
    return sum([joltage(batteries) for batteries in banks])


def parse_banks(banks_input: TextIO) -> list[str]:
    return [l.strip() for l in banks_input]


def main(input_path: Path, part: int):
    with open(input_path, "r") as f:
        banks = parse_banks(f)
    print(total_joltage(banks, part))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    parser.add_argument("--part", "-p", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()

    main(args.input, args.part)
