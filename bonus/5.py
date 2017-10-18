#!/usr/bin/env python3

phrase = input('Введите слово или фразу: ')
consonants = 'gqwrtpsdfhjklzxcvbnm'

for consonant in consonants:
    phrase = phrase.replace(consonant, consonant + 'aig')

print(phrase)
