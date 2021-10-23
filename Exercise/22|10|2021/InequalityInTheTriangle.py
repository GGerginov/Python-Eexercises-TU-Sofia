a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a < b + c or b < a + c or c < a + b:
    print("Yes")
else:
    print("No")