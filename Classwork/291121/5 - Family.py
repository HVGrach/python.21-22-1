# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Father', 'Mother', 'Brother', 'Me']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Father', 183],
    ['Mother', 167],
    ['Brother', 188],
    ['Me', 187]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца -", str(my_family_height[0][1]) + " см")

# Пример вывода на консоль:
# Общий рост моей семьи - ХХ см

# вывод общего роста моей семьи
print("Общий рост моей семьи -", str(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]) + " см")