'''pylypivvv@gmail.com'''
import math

a = float(input('Введіть число: '))
action = str(input('Виберіть одну з запропонованих дій:\n"+"; "-"; "*" (множення); ":" (ділення);\n'
      '"^" (підняття до степеня); "sin"; "cos"; "tg": '))
if action == 'sin':
    print(f'sin({a}) = {math.sin(a)}')
elif action == 'cos':
    print(f'cos({a}) = {math.cos(a)}')
elif action == 'tg':
    print(f'tg({a}) = {math.tan(a)}')
else:
    b = float(input('Введіть наступне число: '))
    if action == '+':
          print(f'{a}+{b} = {a+b}')
    elif action == '-':
          print(f'{a}-{b} = {a-b}')
    elif action == '*':
          print(f'{a}*{b} = {a*b}')
    elif action == ':':
          print(f'{a}:{b} = {a/b}')
    elif action == '^':
          print(f'{a}^{b} = {a**b}')
    else:
          print('Помилкова дія')
