# Создать агрегатные функции для подсчёта общего количества расходов и расходов за месяц.
# Обеспечить соответствующий интерфейс для пользователя.

import sqlite3


conn = sqlite3.connect('./budget.db')
cur = conn.cursor()


def count_expense():
    x1 = input('enter the start date of the period: ')
    x2 = input('enter the end date of the period: ')
    return cur.execute('SELECT sum(summ) FROM budget2 WHERE date BETWEEN ' + x1 + ' AND ' + x2)


y = count_expense()
print(y)

conn.commit()
conn.close()
