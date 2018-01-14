#!/usr/bin/env python3

'''Вариант 3'''

import random as r

def get_words_dict(fname):
    with open(fname, encoding='utf-8') as f:
        words = dict(
        sm = f.readline().split(),
        sf = f.readline().split(),
        sn = f.readline().split(),
        sm_ob_l = f.readline().split(),
        sm_ob_nl = f.readline().split(),
        sf_ob = f.readline().split(),
        sn_ob = f.readline().split(),
        adj = f.readline().split(),
        adv = f.readline().split(),
        vb_ind_ntr = f.readline().split(),
        vb_ind_tr = f.readline().split(),
        vb_imp_ntr = f.readline().split(),
        vb_imp_tr = f.readline().split())
    return words

def create_np_subj(words):
    ends = dict(
    sm = 'ый',
    sf = 'ая',
    sn = 'ое'
    )
    gender = r.choice(['sm', 'sn', 'sf'])
    coin = r.randint(0, 1)
    if coin:
        np_subj = r.choice(words[gender])
    else:
        np_subj = r.choice(words['adj']) + ends[gender] + ' ' + r.choice(words[gender])
    return np_subj

def create_np_obj(words):
    ends = dict(
    sm_ob_l = 'ого',
    sm_ob_nl = 'ый',
    sf_ob = 'ую',
    sn_ob = 'ое'
    )
    gender = r.choice(['sm_ob_l', 'sm_ob_nl', 'sf_ob', 'sn_ob'])
    coin = r.randint(0, 1)
    if coin:
        np_subj = r.choice(words[gender])
    else:
        np_subj = r.choice(words['adj']) + ends[gender] + ' ' + r.choice(words[gender])
    return np_subj

def create_ind_p(words):
    coin = r.randint(0, 1)
    if coin:
        ind_p = create_np_subj(words) + ' ' + r.choice(words['vb_ind_ntr'])
    else:
        ind_p = create_np_subj(words) + ' ' + r.choice(words['vb_ind_tr']) + ' ' + create_np_obj(words)
    return ind_p

def create_imp_p(words):
    coin = r.randint(0, 1)
    if coin:
        if r.randint(0, 1):
            imp_p = create_np_subj(words) + ', ' + r.choice(words['vb_imp_ntr']) + '!'
        else:
            imp_p = r.choice(words['vb_imp_ntr']) + '!'
    else:
        if r.randint(0, 1):
            imp_p = create_np_subj(words) + ', ' + r.choice(words['vb_imp_tr']) + ' ' + create_np_obj(words) + '!'
        else:
            imp_p = r.choice(words['vb_imp_tr']) + ' ' + create_np_obj(words) + '!'
    return imp_p

def make_cap(line):
    new_line = line[:1].upper() + line[1:]
    return new_line

def create_neg_sent(words):
    coin = r.randint(0, 1)
    if coin:
        neg_s = create_np_subj(words) + ' не ' + r.choice(words['vb_ind_ntr']) + '.'
    else:
        neg_s = create_np_subj(words) + ' не ' + r.choice(words['vb_ind_tr']) + ' ' + create_np_obj(words) + '.'
    return make_cap(neg_s)

def create_conj_sent(words):
    coin = r.randint(0, 1)
    if coin:
        conj_s = 'Если ' + create_ind_p(words) + ', ' + create_ind_p(words) + '.'
    else:
        conj_s = 'Если ' + create_ind_p(words) + ', ' + create_imp_p(words)
    return conj_s

def make_all(words):
    sents = [
    create_neg_sent(words),
    create_conj_sent(words),
    make_cap(create_ind_p(words)) + '.',
    make_cap(create_imp_p(words)),
    make_cap(create_ind_p(words)) + '?']
    r.shuffle(sents)
    print(' '.join(sents))


words = get_words_dict('words.txt')
make_all(words)
