# створення масиву в .json
# import json
# from f_019_0_0 import create_person

with open('Persons.json', 'x') as f:
    l = [create_person()]
    json.dump(l, f)
