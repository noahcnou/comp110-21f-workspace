"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730408365"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    xs: list[int] = [9, 11, 13, 22, 24, 2]
    assert only_evens(xs) == [22, 24, 2]


def test_only_evens_with_odd_numbers() -> None:
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_sub_empty_list() -> None:
    xs: list[int] = []
    a: int = 0
    b: int = 0
    assert sub(xs, a, b) == []


def test_sub_negative_and_large_indices() -> None:
    xs: list[int] = [1, 12, 33, 42, 51, 62]
    a: int = 0
    b: int = 6
    assert sub(xs, a, b) == [1, 12, 33, 42, 51, 62]


def test_sub_lots_of_items() -> None:
    xs: list[int] = [1, 5, 8, 52, 74, 77, 92, 104, 111, 500, 1000]
    a: int = 0
    b: int = 10
    assert sub(xs, a, b) == [1, 5, 8, 52, 74, 77, 92, 104, 111, 500]


def test_concat_two_empty_lists() -> None:
    xs: list[int] = []
    vs: list[int] = []
    assert concat(xs, vs) == []


def test_concat_two_lists_combined() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    vs: list[int] = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert concat(xs, vs) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def test_concat_one_empty_lists() -> None:
    xs: list[int] = []
    vs: list[int] = [110]
    assert concat(xs, vs) == [110]