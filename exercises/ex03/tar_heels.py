"""An exercise in remainders and boolean logic."""

__author__ = "730408365"

number = int(input("Enter an int: "))
seven = int(number % 7)
two = int(number % 2)
remainder = 0

if two + seven == 0:
    print("TAR HEELS")
    remainder = remainder + 1
else:
    if number % 2 == 0:
        print("TAR")
        remainder = remainder + 1
    if number % 7 == 0:
        print("Heels")
        remainder = remainder + 1
if remainder == 0:
    print("CAROLINA")
