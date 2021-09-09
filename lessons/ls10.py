"""Challenge Question 1"""

choice: int = int(input("Enter a number: "))

if choice > 75:
    print("A")
else:
    if choice >= 50:
        print("B")
    else: 
        if choice < 25: 
            print("D")
        else:
            print("C")