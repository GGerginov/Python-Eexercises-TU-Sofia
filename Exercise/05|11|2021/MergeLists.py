import random

def merge_list():

    first_list = []
    second_list = []

    seed_list(first_list)
    seed_list(second_list)

    print(first_list)
    print(second_list)

    output_list = []

    for x in range(6):

        if x % 2 == 0:
            output_list.insert(x, first_list[x])

        elif x % 2 == 1:
            output_list.insert(x, second_list[x])

    print(output_list)




def seed_list(list):
    for x in range(6):
        list.append(random.randint(1, 20))





merge_list()




