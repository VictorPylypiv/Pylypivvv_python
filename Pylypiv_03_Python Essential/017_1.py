# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
# арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
# чисел и среднее арифметическое чисел из заданного диапазона.

def arithmetic_mean(my_list):
    return sum(my_list) / len(my_list)


def arithmetic_mean_range(my_list, n1, n2):
    list_range_index = my_list[n1:n2]
    return arithmetic_mean(list_range_index)


l1 = [1, 2, 5, 8, 46, 11, 4]

print(arithmetic_mean(l1))
# print(arithmetic_mean_range(l1, 0, 100))
print(arithmetic_mean_range(l1, 2, 4))
