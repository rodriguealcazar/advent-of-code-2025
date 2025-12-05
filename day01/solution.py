import argparse
from pathlib import Path
from typing import TextIO


def parse_rotations(rotations_file: TextIO) -> list[int]:
    rotations = []
    for r in rotations_file:
        match r[0]:
            case "L":
                rotations.append(-int(r[1:]))
            case "R":
                rotations.append(int(r[1:]))
    return rotations


def method_one(rotations: list[int], start: int) -> int:
    current = start
    zeros = 0
    for r in rotations:
        if (current := current + r) % 100 == 0:
            zeros += 1
    return zeros


def method_two(rotations: list[int], start: int) -> int:
    current = start
    zeros = 0
    for r in rotations:
        if abs(r) > 100:
            zeros += abs(r) // 100
            r = r % 100 if r > 0 else -(abs(r) % 100)

        target = current + r
        if target % 100 == 0:
            zeros += 1
        elif target < 0 and current > 0:
            zeros += 1
        elif target >= 100:
            zeros += 1 
        
        current = target % 100

    return zeros


def main(rotations_file: Path, start: int, method: int):
    with open(rotations_file, "r") as f:
        rotations = parse_rotations(f)
    zeros = method_one(rotations, start) if method == 1 else method_two(rotations, start)
    print(zeros)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    parser.add_argument("--start", "-s", type=int, default=50)
    parser.add_argument("--method", "-m", type=int, default=1)
    args = parser.parse_args()

    main(args.input, args.start, args.method)
