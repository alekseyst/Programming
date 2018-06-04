import re

from string import punctuation

SENT_RE = re.compile(r'[.?!…]')

punctuation = punctuation + '–»«'


def read_file(path):
    with open(path, encoding='utf-8') as inp:
        return inp.read()


def split_sents(text):
    sents = [sent.strip() for sent in SENT_RE.split(text)]
    sents = [sent for sent in sents if sent]
    return sents

def clean_sents(sents, chars):
    table = str.maketrans('', '', chars)
    return [sent.translate(table).strip() for sent in sents]

def add_len(sents):
    out = []
    for sent in sents:
        words = sent.split()
        words = ['{}_{}'.format(word, len(word)) for word in words if word]
        if words:
            out.append(' '.join(words))
    return out

def writelines(path, lines):
    with open(path, 'w', encoding='utf-8') as out:
        for line in lines:
            out.write(line)
            out.write('\n')
def main():
    path = 'example.txt'
    out = 'output.txt'

    text = read_file(path)
    sents = split_sents(text)
    sents = clean_sents(sents, punctuation)
    converted_sents = add_len(sents)
    writelines(out, converted_sents)

main()
