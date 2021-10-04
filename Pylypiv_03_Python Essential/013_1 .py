class Fiesta:
    def __init__(self, year, mileage=0):
        self.year = year
        self.__price_new_car = {
            "2017": 13000,
            "2018": 15000,
            "2019": 16000
        }
        self.__price = self.__get_price(year, mileage)
        self.mileage = mileage

    def __str__(self):
        return f' Your {self.year} car costs $ {self.__price}'

    # def set_mileage(self, mileage):
    #     return self.mileage = mileage

    def __get_price(self, year, mileage):
        if mileage <= 50000:
            return self.__price_new_car.get(year, 0)
        else:
            return self.__price_new_car.get(year) * 0.9 ** int((mileage / 50000))

    @property
    def price(self):
        return self.__price


a1 = Fiesta("2017", 200000)
print(a1)