# Напишите функцию-генератор для получения n первых простых чисел

def prime_num(n):
    l_pn = list(range(n))
    for i in range(2, n):
        for k in range(i*2, n, i):
            l_pn[k] = 0
    l_pn.remove(1)
    for i in l_pn:
        if i:
            yield i


n = 100
a = prime_num(n)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
