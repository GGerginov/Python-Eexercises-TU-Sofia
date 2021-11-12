def sumNums(num1, num2):
      return float(num1+num2)


def subtraction(num1, num2):
      return (num1-num2)


def multiply(num1, num2):
      return float(num1*num2)


def divide(num1, num2):
      return float(num1/num2)

print("Enter operator :"+"\n"
      "+ - sum"+"\n"
      "- - subtract"+"\n"
      "* - multiply"+"\n"
      "/ - divide")

operator =input("Enter operator ")

num1 = float(input("First number = "))
num2 = float(input("Second number = "))



if operator == "+":
      print(sumNums(num1,num2))
elif operator == "-":
      print(subtraction(num1,num2))
elif operator == "*":
      print(multiply(num1,num2))
elif operator == "/":
      print(divide(num1, num2))
else:
      print("Wrong operator")