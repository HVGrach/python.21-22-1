a = input("Введите 8 бит (0/1): ")
if a == "0":
    b = 0
elif a == "1":
    b = 1
else:
    print("это не 0 или 1")
while a != "":
    a = input()
    if a == " ":
        b+=0
    else:
        if a == "1" :
            b += 1
        else:
            b += 0
if b % 2 == 0:
    print("1")
else:
    print("0")

# Evaluation: NOT OK. Программа ест любой ввод, сообщения об ошибке работают не всегда. Иногда вылетает с ошибкой.

# Первый запуск
'''Введите 8 бит (0/1): 1
0
1
2
0
3
1
2
3
10
        <== пробел
        <== пробел
0
        <== пустая строка

# Второй запуск
/python.21-22-1/Homework/November/111121/ex5.py
Введите 8 бит (0/1): 31
это не 0 или 1
043
Traceback (most recent call last):
  File "python.21-22-1/Homework/November/111121/ex5.py", line 16, in <module>
    b += 0
NameError: name 'b' is not defined'''