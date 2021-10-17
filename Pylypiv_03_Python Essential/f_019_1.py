# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных
# чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.

from random import uniform


with open('dir_1/113.txt', 'w') as f:
    for i in range(10000):
        a = str(uniform(-1000000, 1000000)) + '\n'
        f.write(a)


with open('dir_1/113.txt', 'r') as f:
    x = 0
    for line in f:
        x += float(line)
        print(x)
