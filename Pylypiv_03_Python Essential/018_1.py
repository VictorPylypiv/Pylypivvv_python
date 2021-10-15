# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

def set_(s1, s2):
    return s1 & s2


str1 = "Даны две строки"
str2 = "Выведите на экран символы, которые есть в обоих строках"
set1, set2 = set(x for x in str1), {x for x in str2}

print(*set_(set1, set2))

set1.intersection_update(set2)      # інший варіант
print(*set1)
