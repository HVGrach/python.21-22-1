#Введем значения
n = int(input("Введите первое значение"))
m = int(input("Введите второе значение"))

d = 0

# выражаем значение d
if n >= m:
    d = m
else:
    d = n

# ищем наименьшее общее кратное
while m % d != 0 or n % d != 0:
    d = d - 1
print("Наименьшее общее кратное:", d)

# Evaluation: NOT OK. Задание -- найти НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ. В коде -- правильная формула для поиска НОД, но
# пользователь видит комментарий, что это наименьшее общее кратное (НОК). На месте пользователя я бы закрыл программу,
# потому что ищет не то, несмотря на то, что ищет-то она как раз правильно всё.
# В следующий раз не зачту. Внимательнее читаем задание!