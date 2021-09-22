'''pylypivvv@gmail.com'''
# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если
# имя не указано, она должна выводить приветствие для пользователя с Вашим именем.

def hello_name(name = 'Victor'):
    print('Hello ', name, '!', sep='')

hello_name()
hello_name('Petro')