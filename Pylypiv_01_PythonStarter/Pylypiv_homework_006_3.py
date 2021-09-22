'''pylypivvv@gmail.com'''
# 3 Пусть  на  каждую  ступеньку  лестницы  можно  стать  с  предыдущей  или  переступив  через  одну.
#   Определите, сколькими способами можно подняться на заданную ступеньку.


def steps(n):
    if n == 0 or n == 1:
        return 1
    else:
        return steps(n - 1) + steps(n - 2)


n = int(input("Enter the number of stair steps: "))
print(steps(n))
