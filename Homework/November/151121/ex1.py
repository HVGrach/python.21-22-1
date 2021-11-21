min = int(input("Введите мин. значение: "))  # ввод минимального и максимального значений
max = int(input("Введите макс. значение: "))
print('', end="\t")  # отступ
for i in range(min, max + 1):  # первая строчка таблицы умножения
    print(i, end="\t")
print()
for i in range(min, max + 1):  # таблица умножения
    print(i, end="\t")
    for j in range(min, max + 1):
        print(j * i, end="\t")
    print()