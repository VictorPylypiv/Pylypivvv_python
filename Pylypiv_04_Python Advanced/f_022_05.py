# Написать скрипт, который будет выгружать json data в таблицу

import sqlite3


conn = sqlite3.connect('./budget.db')

DATA = 'expenses.json'

conn.execute('')

# for row in conn.execute('SELECT * FROM budget1'):
#     print(row)

conn.commit()
conn.close()
