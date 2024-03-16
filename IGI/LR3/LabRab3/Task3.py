
def task3():
    """
    Counts amount of non-space symbols
    :return: amount of non-space elements in string
    """
    input_str = input('Enter text: ')
    count = 0
    space_count = input_str.count(' ', 0, len(input_str))
    # for ch in input_str:
    #     if ch != ' ':
    #         count += 1

    print(count)
    return len(input_str) - space_count
