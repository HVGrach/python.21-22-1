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

# Начало песни
song_begin = [
    'Катится колобок, а навстречу ему {0}:',
    '— Колобок, колобок! Я тебя съем!',
    '— Не ешь меня, {0}! Я тебе песенку спою, — сказал колобок и запел:',
    'Я Колобок, Колобок!',
    'Я по коробу скребен,',
    'По сусеку метен,',
    'На сметане мешон,',
    'Да в масле пряжон,',
    'На окошке стужон;',
    'Я от дедушки ушел,',
    'Я от бабушки ушел,',
]

# Конец песни
song_end = [
    'И от тебя, {0}, не хитро уйти!',
    'И покатился себе дальше; только {0} его и видел!'
]

# Формат добавляемой строки песни
song_string = 'Я от {0} ушел,'


# Функция, возвращающая песню
def bun_song(animal):
    song = '\n'.join(song_begin + song_end).format(animal)
    song_begin.append(song_string.format(animal))
    return song


# Список животных
animals = ['Заяц', 'Волк', 'Медведь', 'Лиса']
# Выводим песни
for animal in animals:
    print(bun_song(animal), end='\n\n')
