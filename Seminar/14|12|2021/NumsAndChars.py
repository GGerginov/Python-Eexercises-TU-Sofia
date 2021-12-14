num = int(input("Enter n "))

dictionary = {}

try:
    for x in range(num):
        input_num = int(input("Enter your num "))

        str_value = ''

        if input_num == 0:
            str_value = ' '
            dictionary[input_num] = str_value
            continue
        elif input_num <0:
            str_value = ''
            for x in range(abs(input_num)):
                str_value += chr(122- x)
            dictionary[input_num] = str_value

        else:
            for x in range(input_num):
                str_value += chr(x + 97)
                dictionary[input_num] = str_value


except ValueError:
    print("Invalid num")

finally:
    print(dictionary)
