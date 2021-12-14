input = input("Enter your word: ")

list = []

for x in input:
    list.append(ord(x))

asci_codes = tuple(sorted(list))

dictionary = {}

for code in asci_codes:
    dictionary[code] = (code-80)

print(dictionary)
