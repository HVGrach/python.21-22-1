a, b, c = input('1-я сторона: '), input('2-я сторона: '), input('3-я сторона: ')

n = int(a == b) + int(a == c) + int(b == c)

if n == 3:
    print('Равносторонний')
elif n == 1:
    print('Равнобедренный')
else:
    print('Разносторонний')
