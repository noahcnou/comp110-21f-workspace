"""Drawing forests in a loop."""

__author__ = "730408365"

TREE: str = '\U0001F332'
i = int(input("Depth: "))
t = TREE

while i >= 1:
    i = i - 1
    print(t)
    t = t + TREE