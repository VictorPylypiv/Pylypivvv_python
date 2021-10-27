# Создать агрегатные функции для подсчёта общего количества расходов и расходов за месяц.
# Обеспечить соответствующий интерфейс для пользователя.

import sqlite3


conn = sqlite3.connect('./budget.db')
cur = conn.cursor()


def count_expense():
    x1 = input('enter the start date of the period: ')
    x2 = input('enter the end date of the period: ')
    cur.execute('SELECT sum(summ) FROM budget1 WHERE date BETWEEN ' + x1 + ' AND ' + x2)
    amount = cur.fetchall()
    return amount


y = count_expense()
print(f'The amount of costs is {y}')

conn.commit()
conn.close()
