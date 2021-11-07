# заповнення масиву в .json. Нові - в початок списку
import json
from f_019_0_0 import create_person
# from collections import deque


with open('Persons.json', 'r', encoding='utf-8') as f:
    l = json.load(f)

n = int(input('new persons number: '))
l2 = []

with open('Persons.json', 'w', encoding='utf-8') as f2:
    for i in range(n):
        l2.append(create_person())
    for i in l:
        l2.append(i)
    json.dump(l2, f2)

# with open('Persons.json', 'r', encoding='utf-8') as f:    # інший варіант
#     l = json.load(f)
#     d = deque(l)
#
# with open('Persons.json', 'r+', encoding='utf-8') as f:
#     d.appendleft(create_person())
#     l = list(d)
#     json.dump(l, f)
