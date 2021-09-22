'''pylypivvv@gmail.com'''
# 1 Напишите функцию, которая меняет значение глобальной переменной.

def summ_1():
    global x
    x = x ** 3


x = int(input('enter "x": '))
summ_1()
print('new "x" =', x)
