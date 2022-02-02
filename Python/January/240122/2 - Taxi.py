"""Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере 4₽ плюс 0,25₽ за каждые 150 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси. В основной программе должен демонстрироваться результат
вызова функции.

Может быть применен повышающий коэффициент. Используйте рандом для
подстановки коэффициента тарифа (от х1 -- обычный тариф до х2.5 -- повышенный."""
import random


# расчет цены
def taxi_fare(kilometers):
    value = kilometers * 1000 / 150 * 0.25 + 4
    return value


# вызов функции
payment = taxi_fare(kilometers=float(input("enter the kilometers of ur travel - ")))

# коэффицент тарифа
k = random.uniform(1, 2.5)

# вывод полного прайса
print("payment -", round(k * payment, 2), "rubles")
