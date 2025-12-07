import pytest

from day04.solution import accessible_rolls_in_line


@pytest.fixture
def diagram():
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_top_line():
    assert "..xx.xx@x." == accessible_rolls_in_line(["..@@.@@@@.", "@@@.@.@.@@"], 0)
