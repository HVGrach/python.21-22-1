old = input("Возраст человека: ")
sum = 0
if 3 <= int(old) <= 12: # условие
    sum += 150
elif 12 <= int(old) <= 65:
    sum += 450
elif int(old) > 65:
    sum += 250
else:
    sum = sum
while old != '': # цикл, оканчивающий ввод переменных
    old = input()
    if old == '':
        sum += 0
    else:
        if 3 <= int(old) <= 12:  # проверка
            sum += 150
        elif 12 <= int(old) <= 65:
            sum += 450
        elif int(old) > 65:
            sum += 250
        else:
            sum = sum

print(sum)