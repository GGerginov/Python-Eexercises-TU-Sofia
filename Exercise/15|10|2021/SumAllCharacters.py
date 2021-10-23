num = input("")
i = 0
sum = 0.0

while True:
    if i == len(num): break
    current = float(num[i])
    i += 1
    sum += current

print(sum)

