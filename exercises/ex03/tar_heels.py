"""An exercise in remainders and boolean logic."""

__author__ = "730408365"

number = int(input("Enter an int: "))


if(number % 2 == 0):
    print("TAR")
if(number % 7 == 0):
    print("HEELS")
if((number % 2 != 0) and (number % 7 != 0)):
    print("Carolina")
if((number % 2 == 0) and (number % 7 == 0)):
    print("TAR HEELS")