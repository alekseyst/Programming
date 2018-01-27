#!/usr/bin/env python3

'''Вариант 3'''

import collections

def inp_filename():
    return input('Введите название файла: ')

def read_file(filename):
    symbs = r',.?():;"!'
    with open(filename, encoding='utf') as f:
        text = f.read()
        for symb in symbs:
            text = text.replace(symb, '')
        return text.replace("'", ' ').lower().split()

def find_hoods(words):
    hood_dict = {}
    fr_dict = collections.Counter(words)
    for word, freq in fr_dict.items():
        if word.endswith('hoods') and word != 'hoods':
            hood_dict[word[:len(word)-1]] = freq
    for word, freq in fr_dict.items():
        if word.endswith('hood') and word != 'hood' and word not in hood_dict:
            hood_dict[word] = freq
        elif word.endswith('hood') and word != 'hood':
            hood_dict[word] += freq
    return hood_dict

def write_asked(hoods):
    print('Количество слов с суффиксом -hood: ' + str(len(hoods)) + '.')
    if len(hoods) == 0:
        return
    less_common_number = min(hoods.values())
    less_common = [k for k, v in hoods.items() if v == less_common_number]
    print('Минимальная частотность у: '+ ', '.join(less_common) + '.')
    motives = []
    for word in hoods:
        if word.endswith('ihood'):
            motives += [word[:len(word)-5] + 'y']
        else:
            motives += [word[:len(word)-4]]
    print('Мотивирующие основы:', ', '.join(motives) + '.')


write_asked(find_hoods(read_file(inp_filename())))
