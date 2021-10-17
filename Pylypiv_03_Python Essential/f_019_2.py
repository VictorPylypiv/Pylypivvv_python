# Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы он
# сохранял базу ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться с
# модулем shelve, который в данном случае будет весьма удобен и упростит выполнение задания.

import shelve

with shelve.open('f_links.txt') as db:
    link = input("enter your link: ")
    name = input("enter short name: ")
    db[name] = [link]

with shelve.open('f_links.txt', 'r') as db:
    l1 = input("enter the link you want to open: ")
    l0 = 'google.com'
    l2 = db.get(l1, default=l0.split())
    print(*l2)

    # if l1 in db:          # інший варіант
    #     l3 = db.get(l1)
    #     print(*l3)
    # else:
    #     print(l0)

