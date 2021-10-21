"""Unit tests for dictionary functions."""


__author__ = "730408365"


from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_one_pair() -> None:
    """Tests to see if invert can invert a dictionary with one pair of keys."""
    dictionary: dict[str, str] = {'a': 'b'}
    assert invert(dictionary) == {'b': 'a'}


def test_invert_many_pairs() -> None:
    """Tests to see if invert can invert a dictionary with many pairs of keys."""
    dictionary: dict[str, str] = {'cat': 'dog', 'red': 'yellow', 'green': 'blue', 'apple': 'orange', 'bird': 'egg', 'potato': 'fry'}
    assert invert(dictionary) == {'dog': 'cat', 'yellow': 'red', 'blue': 'green', 'orange': 'apple', 'egg': 'bird', 'fry': 'potato'}


def test_invert_same_pair() -> None:
    """Tests to see if invert can work with the same value being in key and value pair."""
    dictionary: dict[str, str] = {'Noah': 'Noah'}
    assert invert(dictionary) == {'Noah': 'Noah'}


def test_favorite_color_one_pair() -> None:
    """Tests to see if the function works with a one pair dictionary."""
    dictionary: dict[str, str] = {"Noah": "green"}
    assert favorite_color(dictionary) == "green"


def test_favorite_color_many_pairs() -> None:
    """Tests to find the most popular color in a dictionary with more than one pair."""
    dictionary: dict[str, str] = {'1': 'green', '2': 'green', '3': 'yellow', '4': 'yellow', '5': 'green'}
    assert favorite_color(dictionary) == 'green'


def test_favorite_color_equal_amount() -> None:
    """Tests to identify a dictionary where there is no most common color."""
    dictionary: dict[str, str] = {'1': 'green', '2': 'white', '3': 'black', '4': 'yellow'}
    assert favorite_color(dictionary) == 'green'

    
def test_count_single_item() -> None:
    """Identifies the amount of times the value is found in the dictionary."""
    input_list: list[str] = ['Hungry']
    assert count(input_list) == {'Hungry': 1}


def test_count_many_items() -> None:
    """Identifies the appearances of many items."""
    input_list: list[str] = ['cake', 'cake', 'cake', 'burger', 'burger', 'fries']
    assert count(input_list) == {'cake': 3, 'burger': 2, 'fries': 1}


def test_count_same_items() -> None:
    """Counts how many times an item is repeated."""
    input_list: list[str] = ['hi', 'hi', 'hi']
    assert count(input_list) == {'hi': 3}