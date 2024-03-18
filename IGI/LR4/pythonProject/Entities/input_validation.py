import math


class Input:

    @staticmethod
    def float_parse(message, lower_bound=-math.inf, upper_bound=math.inf):
        """
        checks user input and trying parse to int value
        :param message:
        :param lower_bound:
        :param upper_bound:
        :return: parsed correct int value
        """
        while True:
            input_str = input(message)
            input_str = input_str.strip()
            try:
                input_str = float(input_str)
                if input_str < lower_bound or input_str > upper_bound:
                    print(f'Your value should be in range ({lower_bound, upper_bound})')
                    continue
            except ValueError:
                print('Input error! You should enter float value')
                continue
            break

        return input_str

    @staticmethod
    def int_parse(message, lower_bound=-math.inf, upper_bound=math.inf):
        """
        checks user input and trying parse to int value
        :param message:
        :param lower_bound:
        :param upper_bound:
        :return: parsed correct int value
        """
        while True:
            input_str = input(message)
            input_str = input_str.strip()
            try:
                input_str = int(input_str)
                if input_str < lower_bound or input_str > upper_bound:
                    print(f'Your value should be in range ({lower_bound, upper_bound})')
                    continue
            except ValueError:
                print('Input error! You should enter integer value')
                continue
            break

        return input_str
