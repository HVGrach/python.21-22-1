import random

m = int(0)  # Переменная для лидирующего числа
n = int(0)  # Переменная для определения кол-ва лидирующих чисел
i = int(0)  # Переменная для i
while i != 100:
    i = random.randint(1, 100)  # Рандомные числа от 1 до 100 включительно
    if i > m:  # Если число больше предыдущих
        print(i, "<== Обновление")
        m = i
        n = n + 1
    else:  # Если число не больше предыдущих
        print(i)
print("Максимальное значение в ряду:", m)
print("Количество смен максимального значения:", n)

# Evaluation: OK