# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
# арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
# чисел и среднее арифметическое чисел из заданного диапазона.

def arithmetic_mean(*numb):
    return sum(numb) / len(numb)


print(arithmetic_mean(5, 17))
print(arithmetic_mean(10, 15, 56, 0))
print(arithmetic_mean(*range(15)))
print(arithmetic_mean(*range(22, 101)))

l1 = [2, 8, 16, 24, 35]
print(arithmetic_mean(*l1))

t1 = (10, 15, 56, 0)
print(arithmetic_mean(*t1))
