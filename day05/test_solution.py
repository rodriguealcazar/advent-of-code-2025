import pytest
from io import StringIO

from day05.solution import (
    fresh_available_count,
    fresh_ids_count,
    is_fresh,
    merged_ranges,
    parse,
    parsed_range,
)


@pytest.fixture
def ranges() -> list[tuple[int, int]]:
    return [(3, 5), (10, 14), (16, 20), (12, 18)]


@pytest.fixture
def ids() -> list[int]:
    return [1, 5, 8, 11, 17, 32]


@pytest.fixture
def input_text() -> StringIO:
    return StringIO(
        """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    )


def test_parsing(input_text, ranges, ids):
    parsed_ranges, parsed_ids = parse(input_text)

    assert ranges == parsed_ranges
    assert ids == parsed_ids


def test_range_parsing():
    assert (3, 5) == parsed_range("3-5")


def test_is_fresh(ranges):
    assert is_fresh(ranges, 5)
    assert is_fresh(ranges, 11)
    assert is_fresh(ranges, 17)
    assert not is_fresh(ranges, 1)
    assert not is_fresh(ranges, 8)
    assert not is_fresh(ranges, 32)


def test_fresh_available_count(ranges, ids):
    assert [5, 11, 17] == fresh_available_count(ranges, ids)


def test_merged_ranges(ranges):
    assert [(3, 5), (10, 20)] == merged_ranges(ranges)
    assert [(3, 5), (9, 21)] == merged_ranges(ranges + [(9, 21)])
    assert [(2, 5), (9, 26)] == merged_ranges(
        ranges
        + [(2, 3), (20, 25), (10, 14), (19, 20), (3, 4), (12, 15), (9, 26), (17, 19)]
    )


def test_fresh_ids_count(ranges):
    assert 14 == fresh_ids_count(ranges)
    assert 16 == fresh_ids_count(ranges + [(9, 21)])
