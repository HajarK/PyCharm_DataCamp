def assignFirstElement(my_list, input):
    print('Start function')
    my_list[0] = input
    print('End function')


if __name__ == '__main__':
    list = [0, 1, 2]
    new_list = list
    input = int(input('Enter a number: '))
    assignFirstElement(list, input)

    print(list)
    print(new_list)