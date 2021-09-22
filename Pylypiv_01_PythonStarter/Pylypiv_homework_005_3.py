'''pylypivvv@gmail.com'''
# Создайте  программу-калькулятор,  которая  поддерживает  четыре  операции:  сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет,  что  хочет  завершить  выполнение  программы.  Каждая  операция  должна  быть
# реализована  в  виде  отдельной  функции.  Функция  деления  должна  проверять  данные  на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

def get_user_action():
    while True:
        action = str(input('Select an action ("+", "-", "*", "/") or "exit": '))
        if action == 'exit':
            print('Goodbye!')
            break
        else:
            calculator(action)

def calculator(action):
    x = float(input('Enter the number: '))
    y = float(input('Enter the next number: '))
    if action == '+':
        result = add(x, y)
    elif action == '-':
        result = sub(x, y)
    elif action == '*':
        result = mult(x, y)
    elif action == '/':
        result = div(x, y)
    else:
        result = 'Wrong action!'
    print('Result =', result)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b:
        return a / b
    else:
        print('error: division by 0')

get_user_action()