# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
# поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
# данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
# после заданного года.

def list_employees(n):
    list_e = []
    i = 0
    while i < n:
        try:
            e1 = input("Enter <Name> <Surname> <department> <year of joining>: ").split()
            e = [e1[0], e1[1], e1[2], e1[3]]
            list_e.append(e)
        except IndexError:
            print("enter again")
        else:
            i += 1
    return list_e


def emp_per_time(list2, year):
    l_t = []
    for i in list2:
        if int(i[3]) >= year:
            l_t.append(i)
    return l_t


def main():
    n = int(input("Enter employees number: "))
    list_e = list_employees(n)
    print("List of employees:")
    for i in list_e:
        print(f' {i[0]} {i[1]}, {i[2]}, joined since {i[3]}')
    y = int(input("Enter year: "))
    lt = emp_per_time(list_e, y)
    print(f'List of employees from {y} year:')
    for i in lt:
        print(f' {i[0]} {i[1]}, {i[2]}, joined since {i[3]}')


if __name__ == '__main__':
    main()
