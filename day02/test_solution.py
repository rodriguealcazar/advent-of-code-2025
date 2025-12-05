import pytest

from day02.solution import invalid_in_range, parse_ranges, sum_invalid_ids


@pytest.fixture
def ranges() -> str:
    return (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124"
    )


def test_parse_ranges(ranges: str):
    assert [
        ("11", "22"), 
        ("95", "115"), 
        ("998", "1012"), 
        ("1188511880", "1188511890"), 
        ("222220", "222224"),
        ("1698522", "1698528"), 
        ("446443", "446449"), 
        ("38593856", "38593862"), 
        ("565653", "565659"),
        ("824824821", "824824827"), 
        ("2121212118", "2121212124")
    ] == parse_ranges(ranges)


def test_invalid_in_range():
    assert [11, 22] == invalid_in_range(["11", "22"])
    assert [99] == invalid_in_range(["95", "115"])
    assert [1010] == invalid_in_range(["998", "1012"])
    assert [1188511885] == invalid_in_range(["1188511880", "1188511890"])


def test_sum_invalid_ids(ranges: str):
    assert 1227775554 == sum_invalid_ids(parse_ranges(ranges))
