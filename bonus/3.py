#!/usr/bin/env python3

cons = 'eyuioa'
word = input('Введите слово или фразу: ').lower()

cons_number = 0
for letter in word:
    if letter not in cons:
        cons_number += 1
    else:
        break

word = word[cons_number:] + word[:cons_number] + 'ay'
print(word)
