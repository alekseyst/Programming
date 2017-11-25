#!/usr/bin/env python3

'''Вариант 3'''

def main():
    filename = input(
    'Введите полное название файла в кодировке utf-8 или Windows 1251'
     '(с путём к нему) или введите название файла в кодировке utf-8 или'
     ' Windows 1251, лежащего в одной папке с программой: ')

    filename = filename.replace('\\', '/')

    for encoding in ['utf-8', 'cp1251']:
        try:
            with open(filename, encoding=encoding) as f:
                text = f.read()
        except UnicodeDecodeError:
            pass

    punctuation = '''!"#$%&'()*+,./:;<=>?@[\]^_`{|}~'''

    for c in punctuation:
        text = text.replace(c, '')

    words = text.split()

    c_one = 0
    c_three = 0



    for word in words:
        if len(word) == 1 and word not in '—–−-':
            c_one +=1
        elif len(word) == 3:
            c_three += 1

    if c_one == 0:
        print('Нет слов длины 1')
    else:
        x = c_three/c_one
        print('Слов длины 3 в', x, 'раз больше, чем слов длины 1.')

try:
    main()
except Exception:
    print('Что-то пошло не так... Возможно, неправильно указано имя файла',
    'или путь к нему или у файла не подходящая кодировка. Если ошибка повторяется, напишите на почту aleksey'
    '-starchenko@mail.ru, мы будем счастливы помочь нашим пользователям!')
