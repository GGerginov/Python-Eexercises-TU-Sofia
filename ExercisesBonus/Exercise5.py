def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2


operators = ['-', '+', '/', '*']

operator = input('Enter operator: ')

if operator in operators:
    try:
        num1 = float(input("Enter your first num: "))
        num2 = float(input("Enter your second num: "))
        print(calculate(num1, num2, operator))
    except ValueError:
        print("Invalid num")


else:
    print("Invalid operator")
