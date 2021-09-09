"""Challenge Question 1"""

choice: int = int(input("Enter a number: "))

if choice > 75:
    print("C")
else:
    if choice >= 50:
        print("D")
    else: 
        if choice < 25: 
            print("A")
        else:
            print("B")