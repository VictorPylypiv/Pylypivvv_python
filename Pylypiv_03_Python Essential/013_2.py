# Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод
# greeting(). Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше
# и вызовите действия этих двух объектов в одной функции (функция hello_friend).


class English:
    @staticmethod
    def greeting():
        return "Hello friend"


class Spanish:
    @staticmethod
    def greeting():
        return "Hola amiga"


def hello_frend():
    print(f'When I hear "{gr_sp.greeting()}" I say "{gr_en.greeting()}"')


gr_en = English()
gr_sp = Spanish()
hello_frend()
