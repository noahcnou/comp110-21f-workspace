"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408365"

from random import randint


fortune_1 = ("You will make it through pledging.")
fortune_2 = ("You will not make it through pledging.")
fortune_3 = ("You will have fun pledging.")
fortune_4 = ("You will not have fun pledging.")

i = int(randint(1, 4))
print("Your fortune cookie says...")
if i == 4:
    print(fortune_4)
else:
    if i == 3:
        print(fortune_3)
    else:
        if i == 2:
            print(fortune_2) 
        else:
            print(fortune_1) 
print("Now, go spread positive vibes!") 
