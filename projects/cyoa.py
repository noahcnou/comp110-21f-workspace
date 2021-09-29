"""Choose your own adventure."""


from random import randint


__author__ = "730408365"

points = int(0)
Happy = str('\U0001F332')


def main() -> None:
    global points
    return greet()


player = str("name")


def greet() -> None:
    global player
    player = input("What is your name? ")
    print("Welcome, " + str(player) + "! Let's see how long it takes you to guess the random number.  Each guess will be tracked.  You can pick between three diffiulty levels: easy, medium, or hard.  You can play as many times as you please!  Have fun!")
    difficulty: int = int(input("Choose Difficulty 1 = Easy, 2 = Med, 3 = Hard."))
    if difficulty == 1:
        return easy()
    if difficulty == 2:
        return med()
    if difficulty == 3:
        return hard()


def easy() -> None:
    answer = (randint(0, 15))
    print("The number is between 0 and 15.")
    while answer == answer:
        guess = int(input("Enter your guess: "))
        global points
        points += 1
        if guess > answer:
            print("Incorrect! Guess Lower.")
        if guess < answer: 
            print("Incorrect! Guess Higher.")
        if guess == answer:
            break

    return final()


def med() -> None:
    answer = (randint(0, 45))
    print("The number is between 0 and 45.")
    while answer == answer:
        guess = int(input("Enter your guess: "))
        global points
        points += 1
        if guess > answer:
            print("Incorrect! Guess Lower.")
        if guess < answer:
            print("Incorrect! Guess Higher.")
        if guess == answer:
            break
    return final()


def hard() -> None:
    answer = (randint(0, 100))
    print("The number is between 0 and 100.")
    while answer == answer:
        guess = int(input("Enter your guess: "))
        global points
        points += 1
        if guess > answer:
            print("Incorrect! Guess Lower.")
        if guess < answer: 
            print("Incorrect! Guess Higher.")
        if guess == answer:
            break
    return final()


def final() -> None:
    print(f"Congratulations {player}, you guessed it in {points} tries! {Happy}")
    again: int = int(input("To play more enter: 1 or to quit enter: 2."))
    if again == 1:
        main()
    else:
        return
    

if __name__ == "__main__":
    main()