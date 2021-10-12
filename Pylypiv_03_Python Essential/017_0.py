# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
# отсортированной в порядке возрастания.

a = sorted(map(int, input("enter numbers: ").split()))
print(*a)

b = sorted(int(i) for i in input("enter numbers: ").split())
print(*b)

l = []
for i in range(5):
    l.append(int(input("enter number: ")))
l.sort()
print(*l)
