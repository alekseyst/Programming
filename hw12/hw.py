import shutil
import os
import re

def print_dirs():
    i = 0
    f_d_list = os.listdir()
    for a in f_d_list:
        if re.search(r'[^а-яА-Я]', a) is None:
            if os.path.isdir(a):
                i += 1
    print('Количество папок, в названиях которых есть только кириллица: ', i)


def find_d_f():
    f_d_list = os.listdir()
    print('Все файлы и папки в директории: ', *set(f_d_list), sep='\n')

print_dirs()
find_d_f()
