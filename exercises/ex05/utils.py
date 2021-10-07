"""List utility functions part 2."""

__author__ = "730408365"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    a: int = 0
    b: int = 0
    if len(xs) == 0:
        return(xs)
    while a <= len(xs):
        if xs[b] % 2 != 0:
            xs.pop(b)
        else:
            b += 1
            a += 1
        while a == len(xs):
            return xs
    return xs


def sub(xs: list[int], x: int, y: int) -> list[int]:
    new: list[int] = []
    if x < 0:
        x = 0
    if y > len(xs):
        y = len(xs)
    if len(xs) == 0:
        return new
    while x < y:
        new.append(int(xs[x]))
        x += 1
    return new


def concat(xs: list[int], vs: list[int]) -> list[int]:
    new: list[int] = []
    while len(xs) + len(vs) == 0:
        return []
    while len(xs) == 0:
        return vs
    while len(vs) == 0:
        return xs
    i: int = 0
    while i < len(xs):
        new.append(int(xs[i]))
        i += 1
    c: int = 0
    while c < len(vs):
        new.append(int(vs[c]))
        c += 1
    return new