"""В русской народной сказке "Колобок" песенка Колобка повторяется при каждой
встрече с очередным животным после слов "Колобок-колобок, я тебя съем!". При каждом повторении
упоминаются все предыдущие существа, от которых Колобок уже "ушёл", и добавляется новое, от которого
он только собирается сбежать.

Напишите функцию bunSong, которая получает на вход имя существа, подставляет его в песенку,
и выводит на экран. Список существ задаётся заранее вне функции. Программа итерируется по списку,
и прогоняет его через функцию для вывода всех куплетов песенки.

Hint:
Используйте отдельный список для хранения строк про животных, от которых уже ушёл главный герой.
Для добавления нового элемента в список используйте метод .append;

-> .append method
Добавляет указанный элемент в конец списка.
list.append(x) -> None
x -- Элемент, который требуется добавить в список.
    my_list = []
    my_list.append(1)
    my_list  # [1]
    my_list.append(3)
    my_list  # [1, 3]
"""

animals = ["ЕГЭ", "Военкомата", "Ипотеки", "Смерть"]#Слова не в Именительном падеже чтобы песня читалась нормально
animals_gone = []
# Функция для подстановки имени в песенку
def bunSong(name):
    # Перечисление тех, от кого ушел колобок
    for animal in animals_gone:
        print(f'Я от {animal} ушел,')
    #     Добавление того, от кого ушел колобок
    animals_gone.append(name)
    print(f'От тебя, {name}, подавно уйду!\n')

# Вызов функции для каждого
for new_animal in animals:
    bunSong(new_animal)
print("Какая славная песенка! — сказала смерть. — Но ведь я, колобок, стара стала, плохо слышу;\n сядь-ка ко мне поближе да пропой еще разок погромче». Колобок подскочил\n и запел ту же песню. «Спасибо, колобок! Славная песенка,\n еще бы послушала! Сядь-ка на мой язычок да пропой в последний разок», — сказала смерть и высунула свой язык;\n колобок прыг ей на язык, а смерть — ам его! и скушала.")