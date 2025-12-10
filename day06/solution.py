import argparse
import re
from functools import reduce
from pathlib import Path
from typing import Literal, TextIO


def parse(problems_input: TextIO) -> tuple[list[list[int]], list[str]]:
    problems = None
    operators = None

    for line in problems_input:
        line = line.strip()

        if not line:
            continue

        parts = re.split(r"\s+", line)

        if not problems:
            problems = [[] for _ in parts]

        if parts[0] in ("*", "+"):
            operators = parts
        else:
            for i, number in enumerate(parts):
                problems[i].append(int(number))
    return problems, operators


def problem_result(numbers: list[int], operator: Literal["*", "+"]) -> int:
    if operator == "+":
        return sum(numbers)
    else:
        return reduce(lambda n, a: n * a, numbers)


def main(problems_input: Path):
    with open(problems_input, "r") as f:
        problems, operators = parse(f)
    print(sum([problem_result(p, o) for p, o in zip(problems, operators)]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
