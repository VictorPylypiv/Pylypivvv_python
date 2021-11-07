# Написать скрипт, который будет выгружать json data в таблицу

import sqlite3
import f_022_05_json_base as jsb


conn = sqlite3.connect('./budget.db')


def replace_data():
    expenses = jsb.get_expenses()
    for key in expenses.keys():
        exp_i = (key, int(expenses[key][0]), expenses[key][1])
        conn.execute('INSERT INTO budget1 (purpose, summ, date) VALUES (?, ? ,?)', exp_i)
    # for row in conn.execute('SELECT * FROM budget1'):
    #     print(row)


replace_data()

conn.commit()
conn.close()
