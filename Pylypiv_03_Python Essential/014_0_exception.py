# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class WrongInput(Exception):
    pass


def magic_number(x):
    if x < 100:
        print("Your number is good")
    else:
        raise WrongInput


while True:
    try:
        x1 = int(input("Enter number less than a hundred: "))
        magic_number(x1)
    except WrongInput:
        print("Wrong number")
