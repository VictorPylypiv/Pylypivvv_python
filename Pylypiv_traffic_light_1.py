# На основе примера создайте алгоритм светофора для пешехода.
# Попросите пользователя ввести количество секунд ожидания.
# Если пользователь вводит некорректное количество секунд,
# то запросите ввод еще раз.
# Каждую итерацию цикла отнимайте единицу от счетчика секунд ожидания,
# когда счетчик ожидания станет равен нулю, то пешеход может идти.


def get_t():
    t = int(input('From 15 to 60 seconds: '))
    while True:
        if 15 <= t <= 60:
            return t
        else:
            t = int(input('fr 15 to 60: '))


def tr_l_ped(seconds):
    wait = seconds
    light = 'red'
    while light == 'red':
        if wait > 0:
            print(f'wait {wait} sec')
            wait -= 1
        else:
            light = 'green'
            print('go!')


def tr_l_dr(seconds):
    wait = seconds
    light = 'red'
    while light == 'red' or light == 'yellow':
        if wait == 1:
            print('get ready')
            light = 'yellow'
            wait -= 1
        if wait > 1:
            print(f'wait {wait} sec')
            wait -= 1
        else:
            light = 'green'
            print('drive')


def main():
    t = get_t()
    tr_l_ped(t)


if __name__ == '__main__':
    main()
