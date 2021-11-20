n = int(input())
m = int(input())
d = min(n, m) # принимает значение меньшего введённого числа
while m % d != 0 or n % d != 0: # Проверка делимости нацело
    d = d - 1
print(d)