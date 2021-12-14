input = input("Enter your word: ")

dictionary = {}

for x in input:
    sum = 0

    for num in str(ord(x)):
        sum += int(num)

    dictionary[ord(x)] = sum

print(dictionary)
