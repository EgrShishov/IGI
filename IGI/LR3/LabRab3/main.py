#Laboratory work 3 - Python's basics
#This program contains tasks from 3rd laboratory work of Selected Chapters of Computer Science
#Version 1.0
#By Egor Shishov
#16.03.2024

from Task1 import task1
from Task2 import task2
from Task3 import task3
from Task4 import task4
from Task5 import task5
from InputValidation import *


#implement simple decorate func
def decorated_menu(input_func):
    def new_menu():
        print('-' * 80)
        input_func()
        print('-' * 80)
    return  new_menu()


@decorated_menu
def menu():
    print('Welcome to labRab 3!')

    while True:
        print('-' * 80)
        choice = int_parse('1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Exit')
        print('-' * 80)
        if choice == 1:
            try:
                x = float_parse('Enter x: ', -1, 1)
                eps = float_parse('Enter accuracy: ')
                result, n = task1(x, eps)
                print(f'x: {x}')
                print(f'n: {n}')
                print(f'My function: {result}')
                print(f'Math F(X): {math.asin(x)}')
                print(f'eps {eps}')
            except ValueError:
                print('Oops! ValueError was caught')
        elif choice == 2:
            max, sum = task2()
            print(f'Maximum of given integers: {max}')
            print(f'Summa : {sum}')
        elif choice == 3:
            print(f'Amount of non space symbols in text: {task3()}')
        elif choice == 4:
            task4()
        elif choice == 5:
            product, total = task5()
            print(f'A product of odd elemets: {product}')
            print(f'A sum of elements between first and last zero elements {total}')
        elif choice == 6:
            print('Good bye!')
            break

        exit = input('Do you want to continue?Y/N: ')
        if exit == 'N':
            print('Good bye!')
            break


if __name__ == '__main__':
    menu()
