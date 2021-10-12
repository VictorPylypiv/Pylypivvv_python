# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
# арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
# чисел и среднее арифметическое чисел из заданного диапазона.

def arithmetic_mean(my_list, n1=0, n2=0):
    if not n2:
        n2 = len(my_list)
    list_range_index = my_list[n1:n2]
    return sum(list_range_index) / len(list_range_index)


l1 = [1, 2, 8, 16, 11, 7]

print(arithmetic_mean(l1))
print(arithmetic_mean(l1, 2, 4))
print(arithmetic_mean(l1, n1=2))
print(arithmetic_mean(l1, n2=4))
