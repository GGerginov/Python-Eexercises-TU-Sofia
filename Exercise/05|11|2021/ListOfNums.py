import random

list = []

# Seed the list
for x in range(6):
  list.append(random.randint(1, 20))

memory = -1

print(list)
for x in range(0,int(len(list)+len(list)/2)+1):

    if memory == -1:
        memory = x
    elif memory != -1:
        list.insert(x,list[memory] + list[x])
        memory = -1

print(list)







