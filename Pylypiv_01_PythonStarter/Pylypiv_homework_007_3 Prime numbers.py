'''pylypivvv@gmail.com'''
# 3 Простым называется число, которое делится нацело только на единицу и само себя. Число 1 не
# считается простым. Напишите программу, которая находит все простые числа в заданном
# промежутке, выводит их на экран, а затем по требованию пользователя выводит их сумму либо произведение


def prime_num1(n):
    lp1 = list(range(n))
    for i in range(2, n):
        for k in range(i*2, n, i):
            lp1[k] = 0
    return lp1


def prime_num_user(a1, a2):
    lp = prime_num1(a2)
    lp.sort()
    for i in range(2, a2):
        if lp[i] >= a1:
            lp2 = lp[i:a2]
            return lp2


def main():
    a1 = int(input("Enter the first number of interval (number #1 > 1): "))
    a2 = int(input("Enter second number of interval (number #2 > number #1): "))
    p = prime_num_user(a1, a2+1)
    print(f'Prime numbers from {a1} to {a2}:')
    for i in p:
        print(i, end=', ')


if __name__ == '__main__':
    main()
