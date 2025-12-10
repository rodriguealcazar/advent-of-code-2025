from io import StringIO

import pytest

from day01.solution import method_one, method_two, parse_rotations


@pytest.fixture
def rotations() -> list[int]:
    return [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]


def test_parsing():
    rotations = StringIO(
        "\n".join(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"])
    )
    assert parse_rotations(rotations) == [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]


def test_method_one_example(rotations):
    assert 3 == method_one(rotations, 50)


def test_method_two():
    assert 1 == method_two([-50], 50)
    assert 1 == method_two([50], 50)
    assert 1 == method_two([-51], 50)
    assert 1 == method_two([51], 50)

    assert 10 == method_two([1000], start=50)

    assert 11 == method_two([1050], start=50)
    assert 11 == method_two([-1050], start=50)
    assert 11 == method_two([1051], start=50)
    assert 11 == method_two([-1051], start=50)
    assert 11 == method_two([1000, 51], start=50)
    assert 11 == method_two([999, 50, 1], start=50)
    assert 11 == method_two([999, 50, 2], start=50)

    assert 10 == method_two([999, 50], start=50)


def test_method_two_example(rotations):
    assert 6 == method_two(rotations, 50)
