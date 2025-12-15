import argparse
from pathlib import Path
from typing import TextIO


def parse(diagram_input: TextIO):
    return [l.strip() for l in diagram_input]


def accessible_rolls_in_line(diagram: list[str], line: int) -> tuple[int, str]:
    lines = [-1, 0, 1]
    if line == 0:
        lines.pop(0)
    if line == len(diagram) - 1:
        lines.pop()

    marked = ""
    accessible = 0
    for i, roll in enumerate(diagram[line]):
        if roll != "@":
            marked = marked + roll
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
            marked = marked + "x"
            accessible += 1
        else:
            marked = marked + "@"

    return accessible, marked


def accessible_in_all_lines(diagram: list[str]) -> tuple[int, list[str]]:
    total_accessible = 0
    new_diagram = []
    for i in range(len(diagram)):
        accessible, new_line = accessible_rolls_in_line(diagram, i)
        total_accessible += accessible
        new_diagram.append(new_line)
    return (total_accessible, new_diagram)


def immediately_accessible_rolls(diagram: list[str]) -> int:
    return accessible_in_all_lines(diagram)[0]


def all_accessible_rolls(diagram: list[str], total_accessible: int = 0) -> int:
    accessible, new_diagram = accessible_in_all_lines(diagram)
    if accessible == 0:
        return total_accessible
    else:
        return all_accessible_rolls(new_diagram, total_accessible + accessible)


def accessible_rolls(diagram: list[str], part: int = 1) -> int:
    if part == 1:
        return immediately_accessible_rolls(diagram)
    if part == 2:
        return all_accessible_rolls(diagram)


def main(diagram_path: Path, part: int):
    with open(diagram_path, "r") as f:
        diagram = parse(f)

    print(accessible_rolls(diagram, part))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    parser.add_argument("--part", "-p", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()

    main(args.input, args.part)
