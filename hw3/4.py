#!/usr/bin/env python3

st = input('Введите слово: ')

for a in range(len(st)):
    print(st[len(st)-a:]+st[:len(st)-a])
