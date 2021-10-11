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

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
