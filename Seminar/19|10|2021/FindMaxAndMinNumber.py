n = int(input("Enter a number n: "))

max = float('-inf')
min = float('inf')

while n >= 1:

    current = int(input("Enter a number : "))

    if current >= max:
        max = current

    if current <= min:
        min = current

    n -= 1


print("Max is ",max)
print("Min is ",min)
