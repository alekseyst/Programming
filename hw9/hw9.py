from re import findall

def get_text():
    fname = input('Введите название файла: ')
    with open(fname, encoding='utf-8') as f:
        return f.read().lower().replace('\n', ' ').replace('\t', ' ')

def find_all(text):
    re_text = r'(?:буд(?:ут|у|е(?:м|те|шь|т))\s)?программир(?:у(?:ем(?:ы(?:й|ми|е|х|м)|ая|ую|о(?:го|му|е|м|й|ю)|[аоы]?)|ющ(?:и(?:й|ми|е|х|м)|ая|ую|е(?:го|му|е|м|й|ю)|[аои]?)|ют|ю|йте|й|е(?:те|шь|т)|я)|ова(?:ть|л[аои]?|вш(?:и(?:й|ми|е|х|м)?|ая|ую|е(?:го|му|е|м|й|ю))|в))(?:ся|сь)?'
    return findall(re_text, text)

def print_words():
    words = find_all(get_text())
    if words:
        print(*set(words), sep=', ')
    else:
        print('Не встретилось ни одной формы слова "программировать"')

try:
    print_words()
except Exception:
    print('Что-то пошло не так...')
