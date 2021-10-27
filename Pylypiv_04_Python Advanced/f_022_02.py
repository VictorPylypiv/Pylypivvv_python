# Создать консольный интерфейс (CLI) на Python для добавления новых записей в базу данных

import sqlite3


conn = sqlite3.connect('./budget.db')


def exp():
    p = input('enter expense item: ')
    s = int(input('summ of expense: '))
    d = input('date of expense: ')
    return (p, s, d)


def in_table():
    while True:
        choice = input('enter <1> for insert expenses: ')
        if choice == '1':
            conn.execute('INSERT INTO budget1 (purpose, summ, date) VALUES (?, ? ,?)', exp())
        else:
            return False


in_table()

# purpose_1 = [
#     ('lesson_materials_1', 10, '05.09.2021'),
#     ('lesson_materials_2', 15, '15.09.2021'),
#     ('lesson_materials_3', 5, '20.09.2021')
# ]
#
# conn.executemany('INSERT INTO budget1 (purpose, summ, date) VALUES (?, ? ,?)', purpose_1)
#
# for row in conn.execute('SELECT * FROM budget1'):
#     print(row)

conn.commit()
conn.close()
