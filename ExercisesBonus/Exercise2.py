input = input("Enter your word: ")

dictionary = {}

for x in input:
    dictionary[x] = ord(x)

print(dictionary)

