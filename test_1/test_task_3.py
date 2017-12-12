def asking():
    inp = []
    while True:
        inp_i = input('Введите название языка:')
        if inp_i == '':
            break
        else:
            inp += [inp_i]
    return inp

def trying(inp):
    with open('Extinct_languages.tsv', encoding='utf-8') as f:
        read_file = f.read().replace('\t', ' - ').strip()
        strings = read_file.split('\n')
        for a in inp:
            for b in strings:
                lang = ''
                if a in b and '(' + a not in b:
                    lang = b
                    break
            if lang  == '':
                print('Языка нет в списке')
            else:
                print(lang)
                    
try:   
    inp = asking()
except Exception:
    print('Ввод названия языка не удался...')

try:
    trying(inp)
except Exception:
    print('С поиском что-то не так...')
