from io import StringIO

import pytest

from day04.solution import accessible_rolls_in_line, all_accessible_rolls, parse


@pytest.fixture
def diagram():
    return StringIO("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""")


@pytest.fixture
def parsed():
    return [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]


def test_top_line():
    assert (5, "..xx.xx@x.") == accessible_rolls_in_line(
        ["..@@.@@@@.", "@@@.@.@.@@"], 0
    )


def test_parsing(diagram, parsed):
    assert parsed == parse(diagram)


def test_all_accessible(parsed):
    assert 43 == all_accessible_rolls(parsed)
