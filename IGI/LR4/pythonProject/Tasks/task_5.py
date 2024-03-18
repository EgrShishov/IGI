import numpy
import numpy as np

#Вставьте первую строку после строки, в которой находится первый встреченный минимальный элемент.
#Вычислить значение медианы первой строки. Вычисление медианы выполнить двумя способами: через стандартную функцию и через программирование формулы.


def task5():
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    array = np.random.rand(n, m)
    print(f'Random np array:\n {array}')

    new_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(new_array)

    min_el = np.min(array)
    print(min_el)

    print('Universal fucntions examples:\n')
    print(array + 5)
    print(array * 5)
    print(array / 5)
    print(array - 5)

    print(np.array([0,2,3,4] + np.array([1,1,-1,2])))

    print('Adding vector to the matrix')
    matrix_array = np.array([[1,2],[3,4]])
    vector_array = np.array([5,6])
    print(matrix_array + vector_array)
    print('-' * 40)

    print('Change array with another array')
    arr2 = np.array([2, 2, 2, 22, -15, -143, -1, -1])
    arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 / arr2)
    print(arr1 * arr2)
    print('-' * 40)

    print('')

    # min_el = array[0][0]
    # for i in range(0, array.shape[0]):
    #     for j in range(1, array.shape[1]):
    #         if array[i][j] < min_el:
    #             min_el = array[i][j]
    #             array = np.append(array, array[0])
    #             break

    print(min_el)
    print(f'New array\n{array}')

    print(array[0])
    print(f'Median value of first row: {np.median(array[0])}')
    print(f'{get_median(array[0])}')

    print(f'Mean {np.mean(array)}') #среднее значение, average имеет дополнительный параметр веса для средневзвешенного значения
    print(f'Mean with axis = 0 {np.mean(array, axis=0)}')
    print(f'Mean with axis = 1 {np.mean(array, axis=1)}')

    print(f'Median with axis = 0 {np.median(array, axis=0)}') #columns
    print(f'Median with axis = 1 {np.median(array, axis=1)}') #rows

    print(f'Corrcoef:\n{np.corrcoef(array)}')

    print(f'Dispersion: {numpy.var(array)}')
    print(f'Dispersion(columns): {numpy.var(array, axis=0)}')
    print(f'Dispersion(rows): {numpy.var(array, axis=1)}')

    print(f'Std : {np.std(array)}')
    print(f'Std(columns): {np.std(array, axis=0)}')
    print(f'Std(rows): {np.std(array, axis=1)}')

def get_median(data: np.ndarray):
    data.sort()
    print(data)
    if len(data) % 2 == 0:
        return (data[(len(data)-1)//2] + data[(len(data)+1)//2]) / 2
    else:
        return data[(len(data)-1)//2]