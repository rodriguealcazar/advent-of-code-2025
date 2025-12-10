import argparse
import math
from collections.abc import Callable
from itertools import batched
from pathlib import Path


def parse_ranges(ranges: str) -> list[tuple[str]]:
    return [tuple(r.split("-")) for r in ranges.split(",")]


def invalids_in_range(id_range: tuple[str], part=1) -> list[int]:
    is_invalid = VALIDATIONS[part]
    invalids = []
    for n in range(int(id_range[0]), int(id_range[1]) + 1):
        if is_invalid(n):
            invalids.append(int(n))
    return invalids


def is_repeating_twice(num: int) -> bool:
    n = str(num)

    if len(n) % 2 != 0:
        return False

    if len(n) == 2:
        if n[0] == n[1]:
            return True

    middle = len(n) // 2
    if n[:middle] == n[middle:]:
        return True

    return False


def divisors(num: int) -> list[int]:
    divisors = []
    # Starting at 1 would include 1 and num itself which we don't need
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)

            div = num // i
            if i != div:
                divisors.append(div)
    return divisors


def is_repeating(number: int) -> bool:
    num = str(number)

    if len(num) < 2:
        return False

    # Special case if repeating 1 character
    if len(set(num)) == 1:
        return True

    for div in divisors(len(num)):
        chunks = {chunk for chunk in batched(num, len(num) // div)}
        if len(chunks) == 1:
            return True
    return False


VALIDATIONS = {1: is_repeating_twice, 2: is_repeating}


def sum_invalid_ids(ranges: list[tuple[str]], part=1) -> int:
    return sum([i for r in ranges for i in invalids_in_range(r, part)])


def main(id_ranges_file: Path, part: int):
    with open(id_ranges_file, "r") as f:
        ranges = parse_ranges(f.readline())
    print(sum_invalid_ids(ranges, part))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    parser.add_argument("--part", "-p", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()

    main(args.input, args.part)
