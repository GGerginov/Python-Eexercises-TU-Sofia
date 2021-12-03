import CalculatorModule

operation = input("Enter operation (ex.sum,subtract,multiply,division): ")


num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))

if operation == "sum":
    print(CalculatorModule.sum(num1, num2))
elif operation == "subtract":
    print(CalculatorModule.subtraction(num1,num2))
elif operation == "multiply":
    print(CalculatorModule.multiply(num1,num2))
elif operation == "division":
    print(CalculatorModule.division(num1,num2))
else:
    print("Invalid command !")





