n = int(input("Введите человеческий возраст собаки: "))
if n<0 or n==0:
    print("Ошибка")
else:
    if n<2:
        print("Собачий возраст собаки:", n*10.5)
    elif n==2:
        print("Собачий возраст собаки 21 год")
    else:
        print("Собачий возраст собаки:", 21+((n-2)*4))