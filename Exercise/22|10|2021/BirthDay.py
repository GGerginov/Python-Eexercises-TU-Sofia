import datetime

x = datetime.datetime.now()

year = int(input("Enter year of birthdate: "))
month = int(input("Enter month of birthdate: "))
day = int(input("Enter day of birthdate: "))

birthday = datetime.datetime(year, month, day)

result1 = abs(x-birthday).days/365

formatted_float = "{:.0f}".format(result1)

print("You are on",formatted_float)
