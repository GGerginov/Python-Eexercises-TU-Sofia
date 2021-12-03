def calcAreaOfSquare(a):
    return float(a * a)

def calcAreaOfRectangle(a, b):
    return float(a * b)

def calcAreaOfTriangle(a, b):
    return float((a * b) / 2)

def calcAreaOfRhombus(a,h):
    return a*h
def calcAreaOfTrapeze(a,b,h):
    return (a+b*h)/2

print("Enter a figure name")
print("Hint: Square,Rectangle,Triangle,Rhombus,Trapeze")

figure = (input("Enter a figure: "))

if figure == "Square":
    a = float(input("Enter a of square: "))
    print(calcAreaOfSquare(a))
elif figure == "Rectangle":
    a = float(input("Enter a of rectangle: "))
    b = float(input("Enter b of rectangle: "))
    print(calcAreaOfRectangle(a, b))
elif figure == "Triangle":
    a = float(input("Enter a of triangle: "))
    b = float(input("Enter b of triangle: "))
    print(calcAreaOfTriangle(a, b))
elif figure == "Rhombus":
    a = float(input("Enter a of rhombus: "))
    h = float(input("Enter h of rhombus: "))
    print(calcAreaOfRhombus(a,h))
elif figure == "Trapeze":
    a = float(input("Enter a of trapeze: "))
    b = float(input("Enter b of trapeze: "))
    h = float(input("Enter h of trapeze: "))

    print(calcAreaOfTrapeze(a,b,h))
else:
    print("Wrong figure")