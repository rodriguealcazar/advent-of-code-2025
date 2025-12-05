import pytest

from day03.solution import largest_joltage, total_joltage

@pytest.fixture
def batteries() -> list[str]:
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]

def test_largest_joltage():
    assert 98 == largest_joltage("987654321111111") 
    assert 89 == largest_joltage("811111111111119")
    assert 78 == largest_joltage("234234234234278")
    assert 92 == largest_joltage("818181911112111")


def test_total_joltage(batteries: list[str]):
    assert 357 == total_joltage(batteries)
