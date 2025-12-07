import argparse
from pathlib import Path
from typing import TextIO


def parsed_range(db_range: str) -> tuple[int]:
    start, end = db_range.split("-")
    return (int(start), int(end))


def parse(text: TextIO) -> tuple[list[tuple[int]], list[int]]:
    ranges = []
    while (l := text.readline().strip()):
        ranges.append(parsed_range(l))

    ids = []
    while (l := text.readline().strip()):
        ids.append(int(l))

    return ranges, ids


def is_fresh(fresh_ids: list[tuple[int]], ingredient_id: int) -> bool:
    for id_range in fresh_ids:
        if ingredient_id >= id_range[0] and ingredient_id <= id_range[1]:
            return True
    return False


def fresh_available(ranges, ids) -> list[int]:
    return [id for id in ids if is_fresh(ranges, id)]


def main(input_path: Path):
    with open(input_path, "r") as f:
        ranges, ids = parse(f)

    print(len(fresh_available(ranges, ids)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
