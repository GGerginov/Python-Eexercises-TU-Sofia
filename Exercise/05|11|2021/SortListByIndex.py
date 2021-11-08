import random

list = []

for x in range(6):
    list.append(random.randint(1, 20))

even_list = []
odd_list = []


for x in list:
    if x %2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)


even_list.sort()
odd_list.sort(reverse=True)

print(list)
print(even_list)
print(odd_list)

iterator = -1

for x in list:
    iterator += 1
    if iterator %2 == 0:
        if len(even_list) != 0:
            list[iterator] = even_list.pop(0)
    else:
        if len(odd_list) != 0:
            list[iterator] = odd_list.pop(0)


print(list)


