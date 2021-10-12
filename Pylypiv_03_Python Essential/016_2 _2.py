# Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл

def numbers_squared_loop(l):
    l2 = []
    for i in l:
        if not i % 2:
            l2.append(i**2)
    return l2


def numbers_squared_gen_1(l):
    l2 = [x ** 2 for x in l if not x % 2]
    return l2


def foo(l):
    return (x ** 2 for x in l if not x % 2)


l1 = [1, 2, 5, 8, 11, 14, 18]

print(numbers_squared_gen_1(l1))
print(numbers_squared_loop(l1))
print(foo(l1))
