# Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed)

def reversed_list(my_list):
    counter = 0
    n = len(my_list)
    for _i in range(n):
        if not n - counter:
            raise StopIteration
        counter -= 1
        yield my_list[counter]


l1 = [1, 2, 5, 8, 11]
a = reversed_list(l1)

while True:
    try:
        print(a.__next__())
    except StopIteration:
        print("The list is empty")
        break


def reversed_list2(my_list):
    n = 0
    for _i in my_list:
        try:
            n -= 1
            yield my_list[n]
        except IndexError:
            return


l2 = reversed_list2(l1)
for i in l2:
    print(i)
