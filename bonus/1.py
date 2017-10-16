#!/usr/bin/env python3

"""
Всем приветь. Я нимнога почитал про Питон. Много интиресных
вищей, оказываеться есть. Ниже есть идеальный код, который
я создал. Ахахахаха.
"""


sum_value = 0
max_value = -float('infinity')
min_value = float('infinity')
while True:
    input_string = input('Введите число: ')
    if input_string == '':
        break

    try:
        input_number = float(input_string)
    except ValueError:
        print('Это не число...')

    max_value = max(max_value, input_number)
    min_value = min(min_value, input_number)
    sum_value += input_number

print(sum_value, min_value, max_value, sep='\n')
