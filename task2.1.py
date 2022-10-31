"""
Перед вами программа, которая вычисляет квадратный.

корень из заданного положительного числа.
"""

from math import sqrt

MESSAGE = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(MESSAGE)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет корректность ввода и возвращает квадрат."""
    if your_number < 0:
        print('Число должно быть больше или равно 0')
        return
    square_root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {square_root}')
    return


print(MESSAGE)
calc(25)
