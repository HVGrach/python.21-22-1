#Получаем все цены и находим их сумму в центах
print('Введите все цены в долларах:')
prices = []
while (price := input()) != '':
    prices.append(float(price))
summa = sum(prices) * 100

#Округляем сумму до ближайших 5 центов
summa =round(summa/5) * 5

#Выводим сумму в долларах
print(f'Округленная сумма: {summa/100}')

# Evaluation: NOT OK. Округление до ПЯТИ центов. То есть последняя цифра может быть либо 5 либо 0.
# Введите все цены в долларах:
# 5
# 3
# 14
# 0
# Округленная сумма: 22.0