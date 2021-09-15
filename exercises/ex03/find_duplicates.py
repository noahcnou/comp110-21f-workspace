"""Finding duplicate letters in a word."""

__author__ = "730396074"

word: str = input("Enter a word: ")
i: int = 0
s: int = 0

while i < len(word):
    h: int = 0
    while h < len(word):
        if h != i:
            if word[h] == word[i]:
                s = s + 1
        h += 1
    i += 1

if s > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")