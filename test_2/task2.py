import re
import collections

def count_gr(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        gr = re.findall(r'<w>.*?gr=\"(.*?)\"', text)
    gr = collections.Counter(gr).most_common()
    with open('out.txt', 'w', encoding='utf-8') as f:
        for a in gr:
            f.write(a[0] + '\n')

count_gr('mystem.xml')
