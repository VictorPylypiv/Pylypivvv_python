'''pylypivvv@gmail.com'''

# Пройтись по диапазону чисел от 0 до 100, выводить все числа, при этом пропустить число 4 и,
# как только цикл достигнет числа 18 - выйти из цикла

x = 0
while x <=100:
    if x == 4:
        x += 1
    elif x != 18:
        print(x, end=' ')
    else:
        break
    x +=1

print()

for i in range(101):
    if i == 4:
        continue
    elif i != 18:
        print(i, end=', ')
    else:
        break
