import json


DATA = 'expenses.json'


def get_expenses():
    try:
        with open(DATA, 'r') as expenses:
            return json.load(expenses)
    except FileNotFoundError:
        return {}


def new_exp():
    purpose = input("expense: ")
    summ = input("summ: ")
    date = input("date:")
    return {purpose: [summ, date]}


def add_exp(expense):
    with open(DATA, 'w') as exp:
        json.dump(expense, exp, indent=4)


def main():
    expenses = get_expenses()
    print("expenses: ", *expenses.keys())

    while True:
        choice = input("Enter <1> for add expense: ")
        if choice == '1':
            expenses.update(new_exp())
            add_exp(expenses)
        else:
            print("wrong choice")


if __name__ == '__main__':
    main()
