directory = input("Enter file directory: ")

try:
    f = open(directory)
except FileNotFoundError:
    print("Wrong directory")
else:
    print(f.read())

