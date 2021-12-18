cost = input("Введите все цены в центах: ")  # cost вводится как строка
sum = int(cost)
# цикл оканчивающий ввод переменных
while cost != "":
    cost = input()
    if cost == "":  # проверка
        sum += 0
    else:
        sum += int(cost)

print("Общая сумма покупки в долларах: ", sum / 100)
if sum % 5 <= 2.5: # округление
    print("К оплате налом: ", (sum - (sum % 5)) / 100)
else:
    print("К оплате налом: ", (sum + 10 - (sum % 5)) / 100)

# Evaluation: OK