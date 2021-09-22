'''pylypivvv@gmail.com'''

# Создайте программу, которая рисует на экране прямоугольный треугольник указанной пользователем высоты
h = int(input("Введіть висоту трикутника: "))

for i in range(1, h):
    for j in range(1, h+1):
        if j == i or j == 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print('* '*h)

print()

y = 1
while y <= h:
    x = 1
    while x <= h:
        print('* ', end='') if x >= h+1-y else print('  ', end='')
        x += 1
    y += 1
    print()
