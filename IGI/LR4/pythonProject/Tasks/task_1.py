import math
import random

from Entities import number as num
from Entities import serializer as serializer


def task1():
    nums = []
    for i in range(0,10):
        nums.append(num.Number(random.randint(-100, 100), random.randint(-100, 100)))

    nums.append(num.Number(12, 2))
    nums.append(num.Number(24, 4))

    serializer.Serializer.serialize_csv('test.csv', nums)

    empty_list = []
    serializer.Serializer.deserialize_csv("test.csv", empty_list)
    print(empty_list)

    serializer.Serializer.serialize_pickle("test.pickle", empty_list)
    new_empty_list = serializer.Serializer.deserialize_pickle("test.pickle")
    print(new_empty_list)
    has_equals = check_eq(nums)
    if has_equals:
        print('The list contains equal numbers')
    else:
        print('There are no equal numbers')

    maximum_value = find_max(nums)
    print(f'maximum value: {maximum_value}')


def find_max(nums: list):
    max_value = num.Number(-math.inf, 1)
    for number in nums:
        for other_num in nums[nums.index(number)+1:]:
            if other_num >= max_value:
                max_value = other_num
    return max_value


def check_eq(nums: list):
    for number in nums:
        for other_num in nums[nums.index(number)+1:]:
            if other_num == number:
                print(number, other_num)
                return True
    return False
