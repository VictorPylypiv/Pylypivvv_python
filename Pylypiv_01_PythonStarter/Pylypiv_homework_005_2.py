'''pylypivvv@gmail.com'''
# Напишите  функцию,  которая  будет  возвращать  результат  наибольшего  общего  делителя  двух
# чисел, переданных в параметры.

def up(a, b):
    if a < b:
        a, b = b, a
    return a, b

def max_common_div(a, b):
    up(a, b)
    while a * b:
        a, b = b, a % b
    else:
        return a

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = max_common_div(a, b)
print(f'Найбільшим спільним дільником чисел {a} і {b} є {c}')
