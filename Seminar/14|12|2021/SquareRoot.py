import math

num1 = int(input("Enter your num: "))

try:
  print(math.sqrt(num1))
except ValueError:
  print("Invalid number")
finally:
  print("Goodbye")


