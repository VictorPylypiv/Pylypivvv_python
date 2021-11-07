# Создать функцию, которая принимает список из элементов типа int, а возвращает новый список из строковых
# значений исходного массива. Добавить аннотацию типов для входных и результирующих значений функции

def str_list(list_int: list):
    list_str: list = []
    for i in list_int:
        list_str.append(str(i))
    return list_str


l1 = [1, 2, 3, 4, 5]
l2 = str_list(l1)
print(l2)
