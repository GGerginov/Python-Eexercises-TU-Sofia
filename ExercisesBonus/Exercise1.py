def create_tuple_by_str(input):
    list = []

    for c in input:
        list.append(c)

    tuple = list

    print(tuple)


def create_tuple_by_str_reverse(input):
    list = []
    for c in input[::-1]:
        list.append(c)

    tuple = (list)

    print(tuple)


def create_tuple_by_codes(input):
    list = []
    for c in input:
        list.append(ord(c))

    tuple = (list)

    print(tuple)


def create_sorted_tuple_by_code(input):
    list = []
    for c in input:
        list.append(ord(c))

    tuple = (sorted(list))

    print(tuple)


string = input()

# 1
create_tuple_by_str(string)
# 2
create_tuple_by_str_reverse(string)
# 3
create_tuple_by_codes(string)
# 4
create_sorted_tuple_by_code(string)
