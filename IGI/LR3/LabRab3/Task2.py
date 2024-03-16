from InputValidation import *


def task2():
    """
    Loop, which inputs integer numbers and calculates maximum of them. 1 - end of loop
    :return: sum of numbers and max element
    """
    sum = 0
    max = -math.inf
    num = math.inf
    while num != 1:
        num = int_parse('Введите целое число: ')
        if num > max:
            max = num
        sum += num
    return max, sum
    # input_sequence = []
    # choice = int(input('1. Generate numbers\n2. Enter number\n'))
    # if choice == 1:
    #     amount = int(input('Enter amount of integers: '))
    #     value_generator(input_sequence, amount)
    # elif choice == 2:
    #     user_input_sequence(input_sequence)
    #return sum(input_sequence, 0), max(input_sequence)
