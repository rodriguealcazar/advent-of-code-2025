from io import StringIO

import pytest

from day06.solution import parse, problem_result


@pytest.fixture
def test_input() -> StringIO:
    return StringIO(
        """123 328  51 64
 45 64  387 23 
  6 98  215 314
*   +   *   + """
    )


@pytest.fixture
def problems() -> list[list[int]]:
    return [[123, 45, 6], [328, 64, 98], [51, 387, 215], [64, 23, 314]]


@pytest.fixture
def operators() -> list[str]:
    return ["*", "+", "*", "+"]


def test_parsing(test_input: StringIO, problems: list[list[int]], operators: list[str]):
    parsed_problems, parsed_operations = parse(test_input)

    assert problems == parsed_problems
    assert operators == parsed_operations


def test_solving_problem():
    assert problem_result([123, 45, 6], "*") == 33210
    assert problem_result([328, 64, 98], "+") == 490
