import argparse
from pathlib import Path
from typing import TextIO


def parsed_range(db_range: str) -> tuple[int, int]:
    start, end = db_range.split("-")
    return (int(start), int(end))


def parse(text: TextIO) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    while l := text.readline().strip():
        ranges.append(parsed_range(l))

    ids = []
    while l := text.readline().strip():
        ids.append(int(l))

    return ranges, ids


def is_fresh(fresh_ids: list[tuple[int, int]], ingredient_id: int) -> bool:
    for id_range in fresh_ids:
        if ingredient_id >= id_range[0] and ingredient_id <= id_range[1]:
            return True
    return False


def fresh_available_count(ranges: list[tuple[int, int]], ids: list[int]) -> list[int]:
    return [id for id in ids if is_fresh(ranges, id)]


def fresh_ids_count(ranges: list[tuple[int, int]]) -> int:
    ranges = merged_ranges(ranges)
    return sum([(r[1] - r[0] + 1) for r in ranges])


def merged_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    def range_start(r: tuple[int, int]) -> int:
        return r[0]

    ranges = sorted(ranges, key=range_start)

    merged_ranges = []
    last_left = 0
    last_right = 0
    for r in ranges:
        if r[0] > last_right:
            merged_ranges.append(r)
            last_left = r[0]
            last_right = r[1]
            continue
        if r[0] <= last_right:
            last_right = max(last_right, r[1])
            merged_ranges[-1] = (last_left, last_right)
            continue
    return merged_ranges


def main(input_path: Path, part: int):
    with open(input_path, "r") as f:
        ranges, ids = parse(f)

    if part == 1:
        print(len(fresh_available_count(ranges, ids)))
    else:
        print(fresh_ids_count(ranges))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    parser.add_argument("--part", "-p", type=int, default=1)
    args = parser.parse_args()

    main(args.input, args.part)
