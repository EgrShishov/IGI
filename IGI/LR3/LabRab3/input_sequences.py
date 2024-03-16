import random
from InputValidation import *


def value_generator(sequence: list, amount: int):
    """
    Generates random numbers and stores them in sequence
    :param sequence:
    :param amount:
    :return:
    """
    while amount:
        amount -= 1
        sequence.append(random.random() * 1e3)


def user_input_sequence(sequence: list, amount):
    """
    Stores user input in list
    :param sequence:
    :param amount
    :return:
    """
    while amount:
        num = float_parse('Введите вещественное число: ')
        sequence.append(num)
        amount -= 1
