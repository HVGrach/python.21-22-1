a = int(input('Уровень шума в децибелах: '))

'''
Таблица уровней громкости:
Отбойный молоток - 130 дБ
Газонокосилка - 106 дБ
Будильник - 70 дБ
Тихая комната - 40 дБ
'''

if a < 40:
    print('Ниже минимального')
elif a == 40:
    print('Тихая комната')
elif a < 70:
    print('Тихая комната - Будильник')
elif a == 70:
    print('Будильник')
elif a < 106:
    print('Будильник - Газонокосилка')
elif a == 106:
    print('Газонокосилка')
elif a < 130:
    print('Газонокосилка - Отбойный молоток')
elif a == 130:
    print('Отбойный молоток')
else:
    print('Выше максимального')
