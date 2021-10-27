# Измените таблиц так, чтобы можно было добавить не только расходы, а и доходы

import sqlite3


conn = sqlite3.connect('./budget.db')

conn.execute('ALTER TABLE budget1 ADD COLUMN income TEXT NOT NULL DEFAULT 0')

# for row in conn.execute('SELECT * FROM budget1'):
#     print(row)

conn.commit()
conn.close()
