# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.

import math


def math_0(l_math):
    x = float(l_math[0])
    op = l_math[1]
    l2 = ["sin", "cos", "tg"]
    if op in l2:
        return math_2(x, op)
    else:
        y = float(l_math[2])
        return math_1(x, op, y)


def math_1(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    elif op == '^':
        return x ** y


def math_2(x, op):
    if op == 'sin':
        return math.sin(x)
    elif op == 'cos':
        return math.cos(x)
    elif op == 'tg':
        return math.tan(x)


def main():
    print("Calculator\n | + | - | * | / |\n | ^ | sin | cos | tg |")
    while True:
        try:
            l1 = input("Enter <number 1> <action> <number 2>: ").split()
            print(math_0(l1))
        except (ValueError, IndexError):
            print("input error")
        except ZeroDivisionError:
            print("error: division by zero")


if __name__ == "__main__":
    main()
