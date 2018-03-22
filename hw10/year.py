'''3 вариант'''

import re

def read_file():
    f_name = input('Введите название файла: ')
    with open(f_name, encoding='utf-8') as f:
        return f.read()

#def read_files(*files):
#    return ''.join(map(read_file, files))


def find_year(text):
    rows_re = r'<th .*?>Год основания</th>(.*?)</td>'
    rows = re.findall(rows_re, text, flags=re.S)
    for row in rows:
        a_re = r'>(.*?)<'
        date = re.findall(a_re, row)
        date = [s.replace('&nbsp;', ' ').strip() for s in date]
        date = [s for s in date if s if r'&#91;' not in s]
        return ' '.join(date)

while True:
    try:
        print(find_year(read_file()))
        break
    except Exception:
        print('Скорее всего, Вы неверно указали имя файла или файл находится не в одной директории с программой. Попоробуйте ещё раз.')
