"""Practice with dictionaries."""

__author__ = "730408365"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Swaps the value and keys."""
    dict_k: list[str] = []
    dict_v: list[str] = []
    new_dict: dict[str, str] = {}
    a: int = 0
    
    for k in dictionary:
        dict_k.append(k)
    
    for v in dictionary:
        dict_v.append(dictionary[v])
    
    while a < len(dict_k):
        new_dict[dict_v[a]] = dict_k[a]
        a += 1
    
    new_dict_k: list[str] = list(new_dict.values())

    if len(new_dict_k) != len(dict_k):
        raise KeyError("Values repeat in this dictionary.")

    return new_dict


def favorite_color(color_dictionary: dict[str, str]) -> str:
    """Which color repeats the most in a dictionary."""
    color: list[str] = []
    present: list[int] = []
    pop: list[int] = []

    for v in color_dictionary:
        color.append(color_dictionary[v])
    
    i: int = 0
    if i < len(color):
        a: int = 1
        b: int = 0
        if b < len(color):
            if b != 1:
                if color[b] == color[i]:
                    a += 1
            b += 1
        present.append(a)
        pop.append(a)
        i += 1

    c: int = 0
    d: int = 1
    if len(pop) > 1:
        if pop[c] > pop[d]:
            pop.pop(1)
        else:
            pop.pop(0)
    
    most_frequent: int = pop[0]
    i: int = 0
    if i < len(present):
        if most_frequent == present[i]:
            return color[i]
        i += 1
    return color[i]


def count(count_item: list[str]) -> dict[str, int]:
    """Counts appearances of word and lists in dictionary."""
    new: dict[str, int] = {}
    i: int = 0
    if i < len(count_item):
        a: int = 1
        b: int = 0
        while b < len(count_item):
            if b != 1:
                if count_item[b] == count_item[i]:
                    a += 1
            b += 1
        new[count_item[i]] = a
        i += 1
    return new