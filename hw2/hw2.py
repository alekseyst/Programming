#!/usr/bin/env python3

newword = ''
word = input('Введите слово: ')
for a in word:
    if a == 'з' or a == 'я':
        continue
    else:
        newword = a + newword
print(newword)
