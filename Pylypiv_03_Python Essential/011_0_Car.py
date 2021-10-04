class Review:
    def __init__(self, rating, text = ""):
        self.rating = rating
        self.text = text

    def __repr__(self):
        return f'rating: {self.rating}, {self.text}'


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.review = Review(5)

    def __repr__(self):
        return f'"{self.model}, {self.year}, color {self.color}", review{self.review}'

    def __str__(self):
        return f'"{self.model} - {self.year}, color {self.color}"'

    def __eq__(self, other):
        return self.model == other.model and self.year == other.year

    # def __new__(self, rating):
    #     self.rating = rating

car_x = Car('Corolla', '2020', 'red')
print(car_x)

class AutoShop: #додати __репр__ список авто (+ їх к-сть) # додавати авто в список
    def __init__(self, car_list):
        self.car_list = car_list

    def __repr__(self):
        return f'In shop present {len(self.car_list)} cars: {self.car_list}'

    def sell_car(self, car): # змінити на вибір машини
        if car in self.car_list:
            return self.car_list.remove(car)
        else:
            print('wrong choose')
            return self.car_list

    def add(self, car):
        return self.car_list.append(car)


CR, CM = 'Corolla', 'Camry'
Y0, Y1 = '2020', '2021'
CB, CW, CG = 'black', 'white', 'grey'

car_01, car_02, car_03 = Car(CR, Y0, CW), Car(CR, Y0, CB), Car(CR, Y0, CG)
car_04, car_05, car_06 = Car(CR, Y1, CW), Car(CR, Y1, CB), Car(CR, Y1, CG)
car_07, car_08, car_09 = Car(CM, Y1, CW), Car(CM, Y1, CB), Car(CM, Y1, CG)

car_list = [car_01, car_02, car_03, car_04, car_05, car_06, car_07, car_08, car_09]
print(car_list)
# print(car_01, car_02, car_03)

shop_1 = AutoShop(car_list)

# car = input(("enter car <model> <year> <color>: "))
# shop_1.add(car)
# print(shop_1)

car_n = Car(CR, Y0, CG)
shop_1.sell_car(car_n)
print(shop_1)

