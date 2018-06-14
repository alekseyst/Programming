'''
В файл inf.csv пишется ответ на задание 1, в names.csv на задание 2, в 2grams.csv на задание 3.
Сами задания выполняются функциями task_1(), task_2(), task_3() соответственно.
В первом задании разделитель в csv -- табуляция.
'''

import os
import re
import collections

def task_1(inp_path):
    files = [files for root, dirs, files in os.walk(inp_path)]
    with open('inf.csv', 'w', encoding='utf-8') as f_w:
        f_w.write("Название файла\tАвтор\tДата создания текста\tЗаголовок\n")
        for f in files[0]:
            with open(os.path.join(inp_path, f), encoding='cp1251') as f_r:
                for a in f_r:
                    if '/head' in a:
                        break
                    if re.search(r'<meta content="(.*?)" name="author"></meta>', a):
                        author = re.search(r'<meta content="(.*?)" name="author"></meta>', a).groups()[0]
                    if re.search(r'<meta content="(.*?)" name="created"></meta>', a):
                        year = re.search(r'<meta content="(.*?)" name="created"></meta>', a).groups()[0]
                    if re.search(r'<meta content="(.*?)" name="header"></meta>', a):
                        header = re.search(r'<meta content="(.*?)" name="header"></meta>', a).groups()[0]
                        for p in '.,':
                            header = header.replace(' ' + p, p)
                f_w.write(f + '\t' + author + '\t' + year + '\t' + header + '\n')


def task_2(inp_path):
    files = [files for root, dirs, files in os.walk(inp_path)]
    n_dict = collections.Counter()
    with open('names.csv', 'w', encoding='utf-8') as f_w:
        f_w.write("имя файла\tнаденное имя\tколичество вхождений\n")
        for f in files[0]:
            with open(os.path.join(inp_path, f), encoding='cp1251') as f_r:
                for a in f_r:
                    if re.search(r'lex="(.*?)"', a):
                        if re.search(r'lex="(.*?)"', a).groups()[0][0].isupper():
                            n_dict[re.search(r'lex="(.*?)"', a).groups()[0]] += 1
            for name, freq in n_dict.most_common():
                 f_w.write(f + '\t' + name + '\t' + str(freq) + '\n')

def task_3(inp_path):
    files = [files for root, dirs, files in os.walk(inp_path)]
    with open('2grams.csv', 'w', encoding='utf-8') as f_w:
        f_w.write("биграмма\tпредложение\n")
        for f in files[0]:
            with open(os.path.join(inp_path, f), encoding='cp1251') as f_r:
                text = f_r.read().split('\n<se>\n')
                for se in text:
                    words = se.split('\n')
                    for n, word in enumerate(words):
                        if 'gr="PR"' in word:
                            if '"S,' in words[n+1] and 'loc' in words[n+1]:
                                twogram = words[n] + words[n+1]
                                twogram = re.sub('<.*?>', '', twogram)
                                for p in '.,!?-"':
                                    twogram = twogram.replace(p, '')
                                sent = re.sub('<.*?>', '', se, flags=re.DOTALL).replace('\n', ' ').replace('  ', ' ')
                                for p in '.,!?-':
                                    sent = sent.replace(' ' + p, p)
                                f_w.write(twogram + '\t' + sent + '\n')


task_1('news')
task_2('news')
task_3('news')
