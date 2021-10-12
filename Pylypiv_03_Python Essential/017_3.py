# Напишите программу, которая вводит с клавиатуры текст и выводит
# отсортированные по алфавиту слова данного текста.

t = input("enter text: ").split(" ")
t.sort()
print(*t)


def get_text():                              # варіант 2
    return input("enter text: ").split(" ")


t = get_text()
t.sort()
print(t)
