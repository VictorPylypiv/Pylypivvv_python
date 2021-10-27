# Сделать таблицу для подсчёта личных расходов со следующими полями: id, назначение, сумма, время.
# .open budget.db

import sqlite3


conn = sqlite3.connect('./budget.db')

conn.execute('''CREATE TABLE budget1(
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    purpose TEXT NOT NULL DEFAULT 0,
    summ INTEGER NOT NULL,
    date TEXT NOT NULL)
''')

conn.execute('INSERT INTO budget1 VALUES (1, "study", 100, "01.09.2021")')
conn.execute('INSERT INTO budget1 (purpose, summ, date) VALUES ("materials", 20, "03.09.2021")')

# for row in conn.execute('SELECT * FROM budget1'):
#     print(row)

conn.commit()
conn.close()

# CREATE TABLE budget1(
# _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# purpose TEXT NOT NULL DEFAULT 0,
# summ INTEGER NOT NULL,
# date TEXT NOT NULL);

# INSERT INTO budget1 VALUES (1, "study", 100, "01.09.2021");
#
# INSERT INTO budget1 (purpose, summ, date),
#        VALUES ("materials", 20, "03.09.2021");
