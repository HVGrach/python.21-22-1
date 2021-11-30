# Создайте списки:

# -----------------------------------------------------------
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

# Список с моей семьёй
my_family = ['Папа', 'Мама', 'Я', 'Бабушка', 'Дедушка']

# -----------------------------------------------------------
# список списков приблизителного роста членов вашей семьи

# Список списков приблизителного роста членов моей семьи
my_family_height = [
    # ['имя', рост],
    ['Папа', 198],
    ['Мама', 169],
    ['Я', 170],
    ['Бабушка', 183],
    ['Дедушка', 167]
]

# -----------------------------------------------------------
# Выведите на консоль рост отца в формате
# Рост отца - ХХ см

# Находим рост отца и выводим его
father_height = next(m for m in my_family_height if m[0] == "Папа")[1]
print(f'Рост отца - {father_height} см')

# -----------------------------------------------------------
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
# Пример вывода на консоль:
# Общий рост моей семьи - ХХ см

# Находим сумму ростов всех членов и выводим её
height_sum = sum(map(lambda m: m[1], my_family_height))
print(f'Общий рост моей семьи - {height_sum} см')