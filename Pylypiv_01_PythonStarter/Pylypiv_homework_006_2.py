'''pylypivvv@gmail.com'''
# 2 Создайте программу, которая проверяет, является ли палиндромом введённая фраза.
# user_sentence = input("Enter Your sentence: ")


def palindrom(sentence):
    n = len(sentence)
    for i in range(n // 2):
        if sentence[i] != sentence[n-1-i]:
            return False
    return True


def check_user_sentense(user_sentence):
    if palindrom(user_sentence):
        print(f'"{user_sentence}" is palindrome')
    else:
        print(f'"{user_sentence}" isn\'t palindrome')


def main():
    user_sentence = input("Enter Your sentence: ")
    check_user_sentense(user_sentence)


if __name__ == '__main__':
    main()

'''
Питання: краще не використовувати оператор "input" в main(),
а провести це окремою функцією як в наступному виконанні?

def get_sentence():
    return input("Enter Your sentence: ")

def main():
    s = get_sentence()
    check_user_sentense(s)
'''
