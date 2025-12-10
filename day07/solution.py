import argparse
from pathlib import Path
from typing import TextIO


def parse(inputs: TextIO):
    start = inputs.readline().strip()
    return {start.index("S")}, [l.strip() for l in inputs]


def moved_beams(beams: set[int], line: str) -> tuple[set[int], int]:
    splits = 0
    for x in set(beams):
        if line[x] == ".":
            continue

        splits += 1

        beams.remove(x)

        if x > 1:
            beams.add(x - 1)
        if x < len(line):
            beams.add(x + 1)

    return beams, splits


def all_splits(start: set[int], lines: list[str]) -> set[int]:
    beams = start
    splits = 0
    for line in lines:
        beams, new_splits = moved_beams(beams, line)
        splits += new_splits
    return splits


def main(diagram: Path):
    with open(diagram, "r") as f:
        start, lines = parse(f)
    print(all_splits(start, lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
