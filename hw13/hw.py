'''Задание 3'''
import collections
import os

def find_most_common(path):
    exts = collections.Counter()
    for root, dirs, files in os.walk(path):
        for f in files:
            if '.' in f:
                exts[f.split('.')[-1]] += 1
    return exts.most_common(1)

print('Чаще всего встречается файл с расширением: ', find_most_common('.')[0][0])
