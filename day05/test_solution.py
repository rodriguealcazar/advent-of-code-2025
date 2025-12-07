import pytest
from io import StringIO

from day05.solution import is_fresh, parse, parsed_range


@pytest.fixture
def ranges() -> list[tuple[int]]:
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
32""")


def test_parsing(input_text, ranges, ids):
    parsed_ranges, parsed_ids = parse(input_text)

    assert ranges == parsed_ranges
    assert ids == parsed_ids


def test_range_parsing():
    assert (3, 5) == parsed_range("3-5")


def test_is_fresh(ranges):
    assert True == is_fresh(ranges, 5)
    assert True == is_fresh(ranges, 11)
    assert True == is_fresh(ranges, 17)
    assert False == is_fresh(ranges, 1)
    assert False == is_fresh(ranges, 8)
    assert False == is_fresh(ranges, 32)
