import math

l1 = input("Калькулятор\n | + | - | * | / |\n | ^ | sin | cos | tg |\nВведіть <число 1> <дія> <число 2>: ").split()


def math_0(l):
    x = float(l[0])
    op = l[1]
    l2 = ["sin", "cos", "tg"]
    if op in l2:
        return math_2(x, op)
    else:
        y = float(l[2])
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
    elif y == None:
        return x


def math_2(x, op):
    if op == 'sin':
        return math.sin(x)
    elif op == 'cos':
        return math.cos(x)
    elif op == 'tg':
        return math.tan(x)

result = math_0(l1)

print(result)
