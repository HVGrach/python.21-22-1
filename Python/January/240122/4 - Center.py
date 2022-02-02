"""Напишите функцию, которая будет принимать в качестве параметров
строку s, а также ширину окна в символах – w. Возвращать функция долж-
на новую строку, в которой в начале добавлено необходимое количество
пробелов, чтобы первоначальная строка оказалась размещена по центру
заданного окна. Новая строка должна формироваться по следующему
принципу:
-> если длина исходной строки s больше или равна ширине заданного
окна, возвращаем ее в неизменном виде;
-> в противном случае должна быть возвращена строка s с ведущими
пробелами в количестве (len(s) – w) // 2 штук.
В вашей основной программе должен осуществляться пример вывода
нескольких строк в окнах разной ширины."""


def center(string, width):
    if len(string) >= width:
        return string
    else:
        spaces = ' ' * ((width - len(string)) // 2)
        return spaces + string


while True:
    string, width = input('Строка: '), int(input('Ширина: '))
    print(f'Результат: "{center(string, width)}"\n')

# OK