import re

def count_body(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
        body = re.findall(r'<body>(.*)</body>', text, flags=re.S)
    with open('out.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(body[0])))


count_body('mystem.xml')
