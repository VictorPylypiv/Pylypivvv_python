# Питання:
#    якщо екземпляр класу створювати в функції, як я зробив в "list_employees",
#    то як надалі робити доступ до цього екземпляру ("e = Employees()")?

class Employees:
    def __init__(self, name, surname, department, year_of_joining):
        self.name = name
        self.surname = surname
        self.dep = department
        self.year = year_of_joining

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.dep}, joined since {self.year}.'

    def get_year(self):
        return self.year


def list_employees(n):
    list_e = []
    i = 0
    while i < n:
        try:
            e1 = input("Enter <Name> <Surname> <department> <year of joining>: ").split()
            e = Employees(e1[0], e1[1], e1[2], e1[3])
            list_e.append(e)
        except IndexError:
            print("enter again")
        else:
            i += 1
    return list_e

a = list_employees(3)
for i in a:
    print(i.name)
