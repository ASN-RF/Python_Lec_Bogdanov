# print(5)
# n = 5
# print (n)

# n = None
# print (n)

# n = 1.89
# print (n)

# n = 'fff'
# print (n)

# n = 5
# print (type(n))

# n = 'fd\"fd"'
# print (n)
# a = 5
# b = 5.89
# c = 'hello'

# print (a)

n = int(input('Введите число: '))
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1
# Повтор заданий как у Sergey Kamyanetsky
