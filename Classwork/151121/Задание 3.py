import random
n = int(input("Введите любое число/цифру чтобы подкинуть монетку, 0 - чтобы закончить программу: "))
a = 0 #Переменная для определения, сколько раз подряд выпал Орёл
b = 0 #Переменная для определения, сколько раз подряд выпала Решка
c = 0 #Переменная для определения, сколько раз подбросили монетку в конкретном цикле
d = 0 #Переменная для определения, сколько всего потребовалось попыток
e = 0 #Сколько раз кончался цикл
while not (n == 0): #Для остановки цикла
    if a == 3 or b == 3: #Чтобы закончить конкретное подбрасывание
        print("(попыток:", c,')')
        n = int(input("Введите любое число/цифру чтобы подкинуть монетку, 0 - чтобы закончить программу: "))
        a = 0
        b = 0
        c = 0
        e = e + 1
    else:
        m = random.randint(1, 2) #Рандом, как ещё
        if m == 1:
            a = a + 1
            b = 0
            c = c + 1
            d = d + 1
            print("О", end=' ') #Специальная строка, чтобы печатала через пустое поле, а не на след. строке
        else:
            b = b + 1
            a = 0
            c = c + 1
            d = d + 1
            print("Р", end=' ') #Специальная строка, чтобы печатала через пустое поле, а не на след. строке
print("Среднее количество попыток:", "%.2f." % (d / e)) #Подсчёт итогового числа попыток

# Evaluation: +-OK. Не очень понятно, зачем нужно каждый раз вводить цифру для продолжения цикла.
# Ну и не пришлось бы писать длиннющие комментарии для каждой переменной, если бы переменные имели осмысленные названия.