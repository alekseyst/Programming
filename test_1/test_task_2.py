'''Случайно сделал вариант 1 вместо варианта 2, прошу проверять вариант 1('''

def fined_problems():
    with open('Extinct_languages.tsv', encoding='utf-8') as f:
        count = 0
        for a in f:
            if a.strip().endswith('Critically endangered'):
                count += 1
        print(count)

try:
    fined_problems()
except Exception:
    print('Что-то пошло не так... Возможно, необходимого файла нет в директории.')

