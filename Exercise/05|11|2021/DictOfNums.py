import random

size = int(input("Enter a size : "))
list = []

# Seed the list
for x in range(1,size+1):
  list.append(x)


dict = {}
test_list = list
test_list.reverse()

for x in range(0,len(list)):
  dict[x] = str(test_list[x])

print(dict)