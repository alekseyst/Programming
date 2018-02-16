'''3 вариант'''

import random

def get_2grams(fname):
    dict_2gr = {}
    with open(fname, encoding = 'utf-8') as f:
        for a in f:
            a = a.strip().split(',')
            dict_2gr[a[0]] = [a[1], a[2]]
    return dict_2gr

def make_quest(dict_2gr):
    two_gr_fr = random.choice(list(dict_2gr.keys()))
    print(two_gr_fr)
    if len(dict_2gr[two_gr_fr][0]) >= len(dict_2gr[two_gr_fr][1]):
        return two_gr_fr + ', ' + dict_2gr[two_gr_fr][0] + ' ...', dict_2gr[two_gr_fr][1], len(dict_2gr[two_gr_fr][0])
    else:
        return two_gr_fr + ', ... ' + dict_2gr[two_gr_fr][1], dict_2gr[two_gr_fr][0], len(dict_2gr[two_gr_fr][1])

def ask():
    print('Перед Вами одна из первых нескольких сотен биграмм, найденных на материале НКРЯ. Вам дана частота биграммы и одно из её слов. Отгадайте другое слово. У Вас есть столько попыток, сколько букв в известном слове. Чтобы остановить игру, введите пусую строку. Подсказка: длина неизвестного слова меньше или равна длине известного.')
    while True:
        two_gr, word, lenth = make_quest(get_2grams('1.csv'))
        print(two_gr)
        for a in range(lenth):
            inp = input('Введите вариант: ')
            if inp == '':
                print('Не отступать!')
                return ''
            if inp == word:
                print('Поздравляем, Вы угадали!')
                break
            else:
                print('Не-а)')
        print('Верный ответ: "' + word + '"')

while True:
    if ask() == '':
        break
