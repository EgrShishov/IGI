import math
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#mpl.use('Agg')
#plt.ion()
os.environ["XDG_SESSION_TYPE"] = "xcb"
np.printoptions(precision=4)

class ArcsinCalculation:

    def __init__(self):
        self.__data = np.array([])

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    def calculate(self, x, eps):
        n = 0
        result = 0.0
        points = np.array([])
        try:
            an = math.factorial(2*n) * x ** (2*n + 1) / (4**n * math.factorial(n) ** 2 * (2*n + 1))
            points = np.append(points, an)
            result = an
            prev = .0
            while abs(an - prev) > eps:
                n += 1
                prev = an
                an = math.factorial(2*n) * x ** (2*n + 1) / (4**n * math.factorial(n) ** 2 * (2*n + 1))
                points = np.append(points, an)
                result += an
                if n == 500:
                    print('Achieved max iteration!')
                    break
        except (OverflowError, ValueError):
            print('Oops! Exception was caught')
        self.__data = points
        return result, n

    def plot(self, x, eps, path_to_file = None):
        X = np.arange(-1, 1, eps)
        y = [math.asin(value) for value in X]
        plt.plot(X,y, color = 'green')

        Y = [self.calculate(value, eps) for value in X]
        plt.plot(X, Y, color='red')

        plt.xlabel('x values from -1 to 1')
        plt.ylabel('my acsin and math.asin functions')
        plt.legend(['math.asin', 'my asin'])
        if path_to_file:
            try:
                plt.savefig(path_to_file)
            except ValueError:
                print('Error! Unsupported type')
        plt.show()

    def get_average(self):
        return np.average(self.__data)

    def get_median(self):
        return np.median(self.__data)

    def get_mode(self):
        vals, counts = np.unique(self.__data, return_counts=True)
        index = np.argmax(counts)
        return vals[index]

    def get_dispersion(self):
        return np.var(self.__data)

    def get_average_square_deviation(self):
        return np.std(self.__data, )


def task3():
    calculation = ArcsinCalculation()
    calculation.calculate(0.433,0.001)
    calculation.plot(0.433, 0.002, 'plot.png')

    print(f'Data: {calculation.data}')

    print(f'Average: {calculation.get_average()}')
    print(f'Median: {calculation.get_median()}')
    calculation.data = np.append(calculation.data, 1.35304562e-02)
    print(f'Mode: {calculation.get_mode()}')
    print(f'Dispersion: {calculation.get_dispersion()}')
    print(f'Average square deviation: {calculation.get_average_square_deviation()}')
