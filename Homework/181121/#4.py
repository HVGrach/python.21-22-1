import math
print("1- Формула виета, 2- Формула Валлиса, 3- Ряд Лейбница")
a, b = int(input("Напишите номер формулы, с помощью которой хотите расчитать число π:")), int(input("До какой цифры после запятой вы хотите округлять:"))
c = int(input("Введите кол-во повторений"))
if a ==1:
    sqrt2 = math.sqrt(2)
    p = 2/sqrt2
    for i in range(c*100):
        sqrt2 = math.sqrt(2 + sqrt2)
        p = p *2/sqrt2
    print(round(p*2),b)
elif a ==2:
    p = (2/1)*(2/3)
    for i in range(2,c*1000000,2):
        p = p*((2+i)/(1+i))*((2+i)/(3+i))
    print(round((p*2),b))
elif a ==3:
    p = 1-1/3+1/5
    for i in range(4,c *1000000,4):
        p +=-1 /(3+i)+1/(5/i)
    print(round((p*4),b))