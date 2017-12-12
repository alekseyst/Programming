'''Переносы на конце строки за символы не считал.'''


def more_then():
    with open('Extinct_languages.tsv', encoding='utf-8') as f:
        for a in f:
            if len(a.strip()) > 35:
                print(a.strip())


try:
    more_then()
except Exception:
    print('Что-то пошло не так... Возможно необходимого файла нет в директории.')
