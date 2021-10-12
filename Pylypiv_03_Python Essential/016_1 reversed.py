# Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed)

def reversed_list(l):
    counter = 0
    n = len(l)
    for i in range(n):
        if not n - counter:
            raise StopIteration
        counter -= 1
        yield l[counter]


l1 = [1, 2, 5, 8, 11]
a = reversed_list(l1)

while True:
    try:
        print(a.__next__())
    except StopIteration:
        print("The list is empty")
        break


def reversed_list2(l):
    n = 0
    try:
        n -= 1
        yield l[n]
    except IndexError:
        return


l2 = reversed_list2(l1)
for i in l2:
    print(i)
