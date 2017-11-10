#!/usr/bin/env python3

st = input('Введите слово: ')

for a in range(0, round(len(st)/2)):
    print(st[a:len(st)-a])
