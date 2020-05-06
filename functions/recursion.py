"""factorial"""


def factorial(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print('factorial')
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))

"""возведение числа а в степень n"""


def my_pow(n: int, a: int):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        return a * my_pow(n-1, a)


print('возведение в степень')
print(my_pow(2, 5))
print(my_pow(3, 10))
print(my_pow(0, 4))
print(my_pow(1, 6))

""""сумма цифр натурального числа"""


def sum_of_digits(n: int):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits((n - n % 10) / 10)


print('сумма цифр натурального числа')

print(sum_of_digits(100))
print(sum_of_digits(1))
print(sum_of_digits(120516))
print(sum_of_digits(99999))

""""количество цифр натурального числа"""


def number_of_digits(n: int):
    if n < 10:
        return 1
    else:
        return 1 + number_of_digits(n / 10)


print('число цифр натурального числа')

print(number_of_digits(100))
print(number_of_digits(1))
print(number_of_digits(120516))
print(number_of_digits(99999))

""""цифровой корень натурального числа"""


def super_digit(n: int):
    if n < 10:
        return n
    else:
        return super_digit(sum_of_digits(n))


print('цифровой корень')

print(super_digit(100))
print(super_digit(1))
print(super_digit(120516))
print(super_digit(99999))
print(super_digit(999999999999))

""""арифметическая прогрессия"""


def arithmetic_progression(first_a: int, step: int, n: int):
    if n == 1:
        return first_a
    else:
        return step + arithmetic_progression(first_a, step, n-1)


print('арифметическая прогрессия')

print(arithmetic_progression(5, 5, 5))
print(arithmetic_progression(5, 2, 1))
print(arithmetic_progression(5, 10, 3))

""""сумма арифметической прогрессии"""


def sum_arithmetic_progression(first_a: int, step: int, n: int):
    if n == 1:
        return first_a
    else:
        return arithmetic_progression(first_a, step, n) + sum_arithmetic_progression(first_a, step, n-1)


print('сцмма арифметической прогрессии')

print(sum_arithmetic_progression(5, 5, 5))
print(sum_arithmetic_progression(5, 2, 1))
print(sum_arithmetic_progression(5, 10, 3))

""""геометрическая прогрессия"""


def geometric_progression(first_b: int, step: int, n: int):
    if n == 1:
        return first_b
    else:
        return step * geometric_progression(first_b, step, n-1)


print('геометрическая прогрессия')

print(geometric_progression(5, 2, 5))
print(geometric_progression(5, 2, 1))
print(geometric_progression(7, 2, 3))

""""сцмма геометрической прогрессии"""


def sum_geometric_progression(first_b: int, step: int, n: int):
    if n == 1:
        return first_b
    else:
        return geometric_progression(first_b, step, n) + sum_geometric_progression(first_b, step, n-1)


print('сцмма геометрической прогрессии')

print(sum_geometric_progression(5, 2, 5))
print(sum_geometric_progression(5, 2, 1))
print(sum_geometric_progression(7, 2, 3))

""""fibonachi"""

def my_fibo(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fibo(n - 1) + my_fibo(n - 2)

print('fibonachi')
print(my_fibo(0))
print(my_fibo(1))
print(my_fibo(2))
print(my_fibo(3))
print(my_fibo(4))
print(my_fibo(5))

"max element of list"


def max_list(arr):
    if arr.length == 1:
        return arr[0]
    else:
        return max_list(arr.pop)