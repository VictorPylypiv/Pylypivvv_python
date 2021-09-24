# На основе примера создайте алгоритм светофора для пешехода.
# Попросите пользователя ввести количество секунд ожидания.
# Если пользователь вводит некорректное количество секунд,
# то запросите ввод еще раз.
# Каждую итерацию цикла отнимайте единицу от счетчика секунд ожидания,
# когда счетчик ожидания станет равен нулю, то пешеход может идти.

# Расширьте функционал программы светофора из предыдущего урока:
# создайте два режима, пешеход и водитель, и переключение между ними.
# запросите у пользователя ввод режима, pedestrian или driver
# Запросите у пользователя ввод нужного режима работы светофора.
#  создайте функцию ожидания светофора для водителя.
    #  Когда ожидание равняется одной секунде - смените свет на желтый
    #  и выведите на экран соответствующее сообщение "get ready!"

print("Traffic light")


def get_m():
    m = input('enter "ped" or "car": ')
    while True:
        if m == 'ped' or m == 'car':
            return m
        else:
            m = input('enter "ped" or "car": ')


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
    m = get_m()
    t = get_t()
    if m == 'ped':
        tr_l_ped(t)
    else:
        tr_l_dr(t)


if __name__ == '__main__':
    main()
