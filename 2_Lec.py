# Задача 2. Последовательность Фибоначчи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

List_1 = []
for i in range(1,10):
    List_1.append(fib(i))
print(List_1)