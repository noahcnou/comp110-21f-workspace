"""Numeric Operators."""

__author__ = "730408365"

Left: int = int((input("Left Side? ")))
Right: int = int((input("Right Side? ")))
print("Left Side: " + str(Left))
print("Right Side: " + str(Right))
print(str(int(Left)) + " ** " + str(int(Right)) + " is " + str(int(Left ** Right)))
print(str(int(Left)) + " / " + str(int(Right)) + " is " + str(float(Left / Right)))
print(str(int(Left)) + " // " + str(int(Right)) + " is " + str(int(Left // Right)))
print(str(int(Left)) + " % " + str(int(Right)) + " is " + str(int(Left % Right)))
