##
# Определяем бит чётности
#
print('Введите группы из восьми бит:')
# Вводим биты пока не будет пустая строка
while (bits := input()) != '':
    # Проверяем ввод
    if len(bits) == 8 and all(c in ('0', '1') for c in bits):
        # Выводим бит чётности
        print(int(bits.count('1') % 2))
    # Неверный ввод
    else:
        print('Error')