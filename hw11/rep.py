'''Вариант 3'''

import re

def read_f(f_name):
    with open(f_name, encoding='utf-8') as f:
        return f.read()

def jazyk2shashlyck(text):
    f = r'\bязык(\w{0,3})\b'
    r = r'шашлык\1'
    F = r'\bЯзык(\w{0,3})\b'
    R = r'Шашлык\1'
    text = re.sub(f, r, text)
    text = re.sub(F, R, text)
    return text.replace('шашлыкове́дение', 'языкове́дение')

def write_f(text):
    with open('out.html', 'w', encoding='utf') as f:
        f.write(text)

write_f(jazyk2shashlyck(read_f('lin.html')))
