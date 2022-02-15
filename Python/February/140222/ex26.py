"""
Организация купила для своих сотрудников все места в нескольких подряд идущих рядах на концертной площадке.
Известно, какие места уже распределены между сотрудниками.
Найдите ряд с наибольшим номером, в котором есть два соседних места, таких что слева и справа от них в том же ряду места
уже распределены (заняты). Гарантируется, что есть хотя бы один ряд, удовлетворяющий условию.
В ответе запишите два целых числа: номер рядя и наименьший номер места из найденных в этом ряду подходящих пар.

В первой строке входного файла находится одно число:
N — количество занятых мест (натуральное число, не превышающее 100000).
В следующих N строках находятся пары чисел: ряд и место выкупленного билета (числа не превышают 100000).

В ответе запишите два целых числа: сначала максимальный номер ряда,
где нашлись обозначенные в задаче места и минимальный номер места.

Пример входного файла:
26_test.txt
Для данного примера ответом будет являться пара чисел 60 и 23.
"""

from itertools import tee

# Считываем весь ввод в список tickets
tickets = []
with open('26.txt') as file:
    n = int(file.readline())
    for _ in range(n):
        tickets.append(tuple(map(int, file.readline().split())))

# Сортируем список по номеру ряда по убыванию и по номеру места по возрастанию
tickets.sort(key=lambda ticket: (-ticket[0], ticket[1]))

# Берём по 2 билета
a, b = tee(tickets)
next(b, None)
tickets_pairs = zip(a, b)

for ticket1, ticket2 in tickets_pairs:
    # Проверяем, что это билеты из одного ряда и между ними 2 свободных места
    if ticket1[0] == ticket2[0] and ticket2[1] - ticket1[1] == 3:
        print(ticket1[0], ticket1[1] + 1)
        break
