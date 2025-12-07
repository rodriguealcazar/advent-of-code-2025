import argparse
from pathlib import Path
from typing import TextIO


def parse(diagram_input: TextIO):
    return [l.strip() for l in diagram_input]


def accessible_rolls_in_line(diagram: list[str], line: int) -> str:
    lines = [-1, 0, 1]
    if line == 0:
        lines.pop(0)
    if line == len(diagram) - 1:
        lines.pop()

    accessible = []
    for i, roll in enumerate(diagram[line]):
        if roll == ".":
            accessible.append(".")
            continue

        columns = [-1, 0, 1]
        if i == 0:
            columns.pop(0)
        if i == len(diagram[0]) - 1:
            columns.pop()

        adjacent = 0
        for y in lines:
            for x in columns:
                if x == 0 and y == 0:
                    continue

                if diagram[line + y][i + x] == "@":
                    adjacent += 1

        if adjacent < 4:
            accessible.append("x")
        else:
            accessible.append("@")

    return "".join(accessible)


def accessible_rolls(diagram: list[str]) -> int:
    accessible = 0
    for i in range(len(diagram)):
        accessible += len(list(filter(lambda x: x == "x", accessible_rolls_in_line(diagram, i))))
    return accessible


def main(diagram_path: Path):
    with open(diagram_path, "r") as f:
        diagram = parse(f)

    print(accessible_rolls(diagram))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
