"""Finding duplicate letters in a word."""

__author__ = "730408365"

word = input("Enter a word: ")
letter_count = 0
count = 0

while letter_count < len(word):
    a = 0
    while a < len(word):
        if a != letter_count:
            if word[a] == word[letter_count]:
                count = count + 1
        a += 1
    letter_count += 1

if count > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")