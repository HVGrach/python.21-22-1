a=int(input("Сумма заказа: "))
b= (a*0.2)
c= (a*0.18)
sum=a+b+c
print("Итог: ", "%2.f" % sum)

# Evaluation: +-OK. Надо было вывести всё -- отдельно налог, отдельно чаевые и только потом итог.