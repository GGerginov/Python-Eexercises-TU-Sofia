def calcAreaOfSquare(a):
      return float(a*a)

def calcAreaOfRectangle(a, b):
      return float(a*b)

def calcAreaOfTriangle(a, b):
      return float((a*b)/2)


print("Enter a num for figure:"+"\n"
      "1 - square"+"\n"
      "2 - rectangle"+"\n"
      "3 - triangle")

n = int(input("Enter a number n: "))

if n == 1:
      a = float(input("Enter a of square: "))
      print(calcAreaOfSquare(a))
elif n == 2:
      a = float(input("Enter a of rectangle: "))
      b = float(input("Enter b of rectangle: "))
      print(calcAreaOfRectangle(a,b))
elif n == 3:
      a = float(input("Enter a of triangle: "))
      b = float(input("Enter b of triangle: "))
      print(calcAreaOfTriangle(a,b))
else:
      print("Wrong key")
