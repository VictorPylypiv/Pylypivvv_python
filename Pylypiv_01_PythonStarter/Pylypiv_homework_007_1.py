'''pylypivvv@gmail.com'''
# 1 Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка, а
# также сумму и среднее арифметическое его значений.
l1 = [1, 4, 7, 34, -5, 8]


def l_min(l):
    a_min = l[0]
    for i in range(len(l)):
        if l[i] < a_min:
            a_min = l[i]
    return a_min


def l_max(l):
    a_max = l[0]
    for i in range(len(l)):
        if l[i] > a_max:
            a_max = l[i]
    return a_max


def l_sum(l):
    a_sum = l[0]
    for i in range(1, len(l)):
        a_sum += l[i]
    return a_sum


a1, a2, a3 = l_min(l1), l_max(l1), l_sum(l1)
a4 = round(l_sum(l1) / len(l1), 3)

print(f'For list {l1} minimum value is {a1}, maximum value is {a2},\n'
      f'sum of values {a3}, average {a4}')

b1, b2, b3,  = min(l1), max(l1), sum(l1)
print(a1 == b1 and a2 == b2 and a3 == b3)
