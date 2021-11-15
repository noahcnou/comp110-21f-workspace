"""Examples of optional paramaters and Union types."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Life from Sector " + str(name)
    return greeting


# Single-argument
print(hello("Sally"))

# No arguments!
print(hello())

# int argument
print(hello(110))
print(hello(3.14))