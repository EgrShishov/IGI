from functools import reduce
from input_sequences import *
from InputValidation import *


def task5():
    """
    Finds product of two elements with odd indexes and total sum of all elements between first and last zero positions
    :return: product and sum
    """
    float_sequence = []
    choice = int_parse('Which type of entering your choice?\n1.Generate sequence\n2.User input\n', 1, 2)
    amount = int_parse('How much elements do you need?: ', 1)

    if choice == 1:
        value_generator(float_sequence, amount)
    elif choice == 2:
        user_input_sequence(float_sequence, amount)
    print(f'List: {float_sequence}')

    product = reduce(lambda x, y: x * y, float_sequence[::2])
    total = .0

    if float_sequence.count(0):
        start = float_sequence.index(0, 0)
        end = float_sequence.index(0, start + 1)
        total = reduce(lambda x, y: x + y, float_sequence[start:end])
    return product, total
