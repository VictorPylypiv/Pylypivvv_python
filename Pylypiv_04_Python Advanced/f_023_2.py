# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.

l1 = [i for i in range(10)]

for i in map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, l1)):
    print(i)
