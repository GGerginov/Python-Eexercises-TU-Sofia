def findMaxInlist(input_list):

    max = float('-inf')
    index = -1


    for x in input_list:
        if x>max:
            max = x
            index = input_list.index(x)

    print([max, index])



findMaxInlist([2,3.4,8.99,123])

