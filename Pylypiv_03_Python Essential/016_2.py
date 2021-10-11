# Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл

def numbers_squared_loop(l):
    l2 = []
    for i in l:
        if not i % 2:
            l2.append(i**2)
    return l2


def numbers_squared_gen_1(l):
    l2 = [x ** 2 if not x % 2 else None for x in l]
    return l2


def numbers_squared_gen_2(l):
    for i in l:
        if not i % 2:
            yield i**2


l1 = [1, 2, 5, 8, 11, 14, 18]

print(numbers_squared_gen_1(l1))

print(numbers_squared_loop(l1))

a = numbers_squared_gen_2(l1)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())
