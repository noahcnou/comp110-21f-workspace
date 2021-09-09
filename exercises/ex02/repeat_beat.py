"""Repeating a beat in a loop."""

__author__ = "730408365"

sound = input("What beat do you want to repeat? ")
repetitions = int(input("How many times do you want to repeat it? "))
repeat_count = repetitions
s = str(sound)

while repetitions > 1:
    repetitions = repetitions - 1
    s = s + " " + sound

if repetitions >= 1:
    print(s)

if repetitions <= 0:
    print("No beat...")
