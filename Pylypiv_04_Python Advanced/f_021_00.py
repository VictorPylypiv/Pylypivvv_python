import json

PERSONS = 'data/cbs_students.json'


def get_persons():
    try:
        with open(PERSONS, 'r') as persons:
            return json.load(persons)
    except FileNotFoundError:
        return {}


def new_person():
    name = input("name: ")
    lastname = input("lastname: ")
    name1 = name + " " + lastname
    age = input("age:")
    # gender = input("gender: ")
    return {name1: age}


def add_person(person):
    with open(PERSONS, 'w') as persons:
        json.dump(person, persons, indent=4)


def main():
    persons = get_persons()
    print("Students CBS are: ", *persons.keys())

    while True:
        choice = input("Enter <1> for add new student, <2> for get the age an existing one: ")
        if choice == '1':
            persons.update(new_person())
            add_person(persons)
        elif choice == '2':
            name = input("enter <name lastname> of student: ")
            print(persons.get(name))
        else:
            print("wrong choice")


if __name__ == '__main__':
    main()
