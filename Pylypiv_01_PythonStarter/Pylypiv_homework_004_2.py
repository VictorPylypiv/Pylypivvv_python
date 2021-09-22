'''pylypivvv@gmail.com'''

# В предложении “Hello world” заменить все буквы “o” на “a” , а буквы “l”  на “e”

string = 'Hello, world'

string_new = ''
x = 0
while x <len(string):
    if string[x] == 'o':
        string_new += 'a'
    elif string[x] == 'l':
        string_new += 'e'
    else:
        string_new += string[x]
    x +=1

print(string_new)

string_new_2 = ''
for i in string:
    if i == 'o':
        string_new_2 += 'a'
    elif i == 'l':
        string_new_2 += 'e'
    else:
        string_new_2 += i

print(string_new_2)

