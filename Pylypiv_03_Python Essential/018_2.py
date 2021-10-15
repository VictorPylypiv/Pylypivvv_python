# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована
# возможность ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию

def short_link():
    link = input("enter your link: ")
    name = input("enter short name: ")
    return {name: link}


s_link = short_link()

print(s_link.get(input("enter the link you want to open: ")))


# def short_link_1(link, name):
#     return {name: link}
#
#
# link1 = "https://www.google.com.ua/maps/@49.8397338,24.0352189,12.71z"
# short_name1 = "google.map.lviv"
# s_link = short_link_1(link1, short_name1)
# print(s_link.get("google.map.lviv"))
