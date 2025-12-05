import argparse
from pathlib import Path


def parse_ranges(ranges: str) -> list[tuple[str]]:
    return [tuple(r.split("-")) for r in ranges.split(",")]


def invalid_in_range(id_range: tuple[str]) -> list[int]:
    invalids = []
    for n in range(int(id_range[0]), int(id_range[1]) + 1):
        n = str(n)

        if len(n) % 2 != 0:
            continue

        if len(n) == 2:
            if n[0] == n[1]:
                invalids.append(n)
            continue

        middle = len(n) // 2
        if n[:middle] == n[middle:]:
            invalids.append(n)

    return [int(n) for n in invalids]
    

def sum_invalid_ids(ranges: list[tuple[str]]) -> int:
    return sum([i for r in ranges for i in invalid_in_range(r)])


def main(id_ranges_file: Path):
    with open(id_ranges_file, "r") as f:
        ranges = parse_ranges(f.readline())
    print(sum_invalid_ids(ranges))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path)
    args = parser.parse_args()

    main(args.input)
