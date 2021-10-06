"""List utility functions."""

__author__ = "730408365"


def all(xs: list[int], x: int) -> bool:
    """A test to see if an any number is equal on the list."""
    i: int = 0
    f: int = 0
    while i < len(xs):
        if xs[i] == x:
            return False
        if f == len(xs):
            return True
        return False


def is_equal(xs: list[int], zs: list[int]) -> bool:
    """A test to see if two lists equal each other."""
    i: int = 0
    b: int = 0
    if len(xs) == len(zs):
        while i < len(xs):
            if xs[i] == zs[i]:
                b += 1
        if b == len(xs) and len(zs):
            return True
        else:
            return False
    else:
        return False


def max(input: list[int]) -> int:
    """Function to find the largest value in list."""
    d: int = 0
    dz: int = 1
    while len(input) > 1:
        if input[d] > input[dz]:
            input.pop(1)
        else:
            input.pop(0)
        if len(input) == 0:
            raise ValueError("max() arg is an empty list")
    return input[0]