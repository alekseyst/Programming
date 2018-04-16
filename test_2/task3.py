import re
import collections

def count_V(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        V = re.findall(r'<w>.*?gr=\"V.*?сов.*?ед', text) + re.findall(r'<w>.*?gr=\"V.*?ед.*?сов', text)
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(V)))


count_V('mystem.xml')

def get_body(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        body = re.findall(r'<body>(.*)</body>', text, flags=re.S)
        body = body[0].strip().split('\n')
        return body

def make_csv(tag):
    with open('out.csv', 'w', encoding='utf-8') as f:
        for a in tag:
            b = re.match(r'<w><ana lex=\"(.*?)\"', a)
            if b:
                f.write(b.groups()[0]+'\n')

make_csv(get_body('mystem.xml'))
