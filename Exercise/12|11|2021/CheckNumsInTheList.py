mylist = [2, 23, 31, 5, 11, 15, 4]
num = 15


def myFunc(mylist, num):
    for i in range(len(mylist)):
        if mylist[i] > num:
            mylist[i] = 0

    return mylist

myFunc(mylist, num)
print(mylist)