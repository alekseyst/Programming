#!/usr/bin/env python3

try:
    gradusy_celsija = float(input('Введите количество градусов Цельсия: '))
    print('Градусов Кельвина: ', gradusy_celsija + 273.15)
    print('Градусов по Фаренгейту: ', gradusy_celsija * 9 / 5 + 32)
except ValueError:
    print('Градусы Цельсия это число!')
