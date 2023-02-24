# def f(x):
#     return x*x

# a = f   # переменная, которая хранит в себе ссылку на функцию
# print(a(5))
# print(f(5))


# calk1 = lambda a: a+a   # def calk1 (a):
#                         #     return a+a

# calk2 = lambda a: a*a  # def calk2 (a):
# return a*a

# def math (op, x):
#     print (op(x))

# math (lambda a: a+a, 5)

# Задача 1. В списке хранятся числа. Нужно выбратьтолько четные числа и составить список пар
# (число; квадрат числа)

# Пример: 1 2 3 5 8 15 23 28
# Получить: [(2,4), (8,64), (38,1444)]

# Spisok = [1, 2, 3, 5, 8, 15, 23, 38]
# Spisok_rez = []
# Rezult_spisok = [(i, i*i) for i in Spisok if i % 2 == 0]
# print(Rezult_spisok)



# def select (f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select (int, data)
# print (res)
# res = where (lambda x: x%2 == 0, res)
# print (res)
# res = select (lambda x: (x, x**2), res)
# print (res)

#  --------- MAP ------
# list_1 = list(map(int, input('Введите Ваш набор чисел: ').split()))
# print(list_1)

# import os
# print (os.getcwd())

Dlina = {4, 4, 4}
print (len(set(Dlina)))