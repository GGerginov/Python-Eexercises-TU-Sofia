import math

num = int(input("Enter your num: "))

if num<0:
    raise ValueError("Number must be greater than zero")
else:
    print(math.sqrt(num))
    print("Goodbye")

