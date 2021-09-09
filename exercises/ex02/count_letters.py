"""Counting letters in a string."""

__author__ = "730408365"

word = input("Enter a word: ")
letter = input("What letter do you want to search for? ")
count = 0
while len(word) != 1:
    if letter == word[0]:
        count = count + 1
    word = word[1:]
print("Count:", count) 
