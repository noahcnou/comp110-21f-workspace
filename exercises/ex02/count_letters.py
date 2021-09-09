"""Counting letters in a string."""

__author__ = "730408365"

letter = input("What letter do you want to search for? ")
word = input("Enter a word: ")
count = 0
while len(word) != 0:
    if letter == word[0]:
        count = count + 1
    word = word[1:]
print("Count:", count) 
