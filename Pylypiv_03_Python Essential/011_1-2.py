class Book:
    def __init__(self, name, ganre, year):
        self.name = name
        self.ganre = ganre
        self.year = year

    def __str__(self):
        return f'{self.name}, {self.ganre} from {self.year} is my favorite'

    def change_ganre(self):
        color = input('color ')
        if color == 'red':
            self.ganre = 'detective'
        else:
            self.year += '-II'
        # return self.ganre, self.year

    def comment(self, rating='', review=''):
        rating, review = input("Your rating "), input("Your review ")
        self.rating, self.review = rating, review
        return f'{self.name} - {rating}, {review}'


book_1 = Book('Abc', ganre='comedy', year='2010')
print(book_1)
print(book_1.comment())
book_1.change_ganre()
print(book_1)
