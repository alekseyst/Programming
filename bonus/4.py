#!/usr/bin/env python3

phrase = input('Введите слово или фразу: ')
vowels = 'уеэоаыяиюё'

for vowel in vowels:
    phrase = phrase.replace(vowel, vowel + 'с' + vowel)

print(phrase)
