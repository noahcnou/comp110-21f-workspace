"""Finding duplicate letters in a word."""

__author__ = "730408365"

word: str = input("Enter a word: ")
i: int = 0
a: int = 0

while i < len(word):
    s: int = 0
    while s < len(word):
        if s != i:
            if word[s] == word[i]:
                a = a + 1
        s += 1
    i += 1

if a > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")