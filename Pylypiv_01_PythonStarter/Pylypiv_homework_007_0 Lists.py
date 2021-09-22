'''pylypivvv@gmail.com'''
# Создайте список, введите количество его элементов и сами значения, выведите эти значения на
# экран в обратном порядке

l = list(range(6))
n = len(l)
l2 = []
l3 = [0]*n
l4 = []
l5 = []

for i in range(n):
    l2.append(l[n-1-i])

for i in range(n):
    l3[i] = l[n-1-i]

for i in range(n-1, -1, -1):
    l4.append(l[i])

for i in reversed(range(n)):
    l5.append(l[i])

for i in range(n):
    print(l[n-1-i], end=' ')
print()

for i in range(n-1, -1, -1):
    print(l[i], end=' ')
print()

for i in range(n)[::-1]:
    print(l[i], end=' ')
print()

for i in reversed(range(n)):
    print(l[i], end=' ')
print()

l.reverse()

print(l2, l3, l4, l5)
print(l)

l2 = []
l6 = list(range(10,16))
for i in l6[::-1]:
    print(i, end=' ')
l2.append(i)

print('2')

print(list(reversed(range(5))))

l7 = list(reversed(range(6, 10)))

print(l6[i] for i in reversed(range(len(l6))))
