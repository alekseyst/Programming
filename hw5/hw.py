#!/usr/bin/env python3

'''Вариант 3'''

inp = 'a'
coun = 0

with open('out.txt', 'w', encoding = 'utf-8') as f:
    while inp:
        coun += 1
        inp = input('Введите слово: ')
        f.write(inp[coun:] + '\n')
