'''pylypivvv@gmail.com'''
import math

voice = str(input('What did the animal said? '))
if voice == 'Meow':
    print('This is a cat!')
elif voice == 'Bark':
    print('This is a dog!')
else:
    print('This is un unknown animal!')


x = float(input('Enter "x": '))
print(f'y = {x}' if x > math.pi or x < -math.pi else f'y = {round(math.cos(3*x), 3)}')


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
