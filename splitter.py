# -*- coding: utf-8 -*-

import codecs
import re


def list_tokens():
    f = codecs.open(u'podcorpus_Sasha_Grisha_Tanya.txt', u'r', u'utf-8')
    a = f.read()
    text = re.sub(u'\r\n+?', u' ', a, flags=re.U)
    text = re.sub(u' +?', u' ', text, flags=re.U)
    text = re.sub(u'( [А-ЯЁ] )\.', u' \1Ѯ', text, flags=re.U)
    tokens = text.split(u' ')
    return tokens


def sent(arr):
    tokens = []
    for i in range(0, len(arr)):
        tokens.append(arr[i])
        if arr[i] in '.?!':
            if i < len(arr) - 1:
                if arr[i+1].istitle() or arr[i+1].isupper():
                    tokens.append('<sent>')
    output = '\r\n'.join(tokens)
    output = output.replace(u'ѫ', u',')
    output = output.replace(u'ω', u':')
    output = output.replace(u'…', u'...')
    output = output.replace(u'ѹ', u'/')
    output = output.replace(u'Ω', u'?')
    output = output.replace(u'ѧ', u'.')
    output = output.replace(u'Ѯ', u'.')
    output = output.replace(u'<sent>', u'')
    output = re.sub(u'\r\n\r\n\r\n', u'\r\n\r\n', output, flags=re.U)
##    for token in tokens:
##        print token
    w = codecs.open(u'tokens.txt', u'w', u'utf-8')
    w.write(output)
    w.close()

sent(list_tokens())    
                
                


##def sent():
##    arr_sent = []
##    f = codecs.open('podcorpus_Sasha_Grisha_Tanya.txt', 'r', 'utf-8')
##    a = f.read()
##    ohne_initials = re.sub(u'([^а-яё][А-ЯЁX]) \.', u'\1\.', a, flags = re.U)
##    ohne_abbrev = re.sub(u'([а-яё]+?) \. ([а-яё]+?)', u'\1\. \2', ohne_initials, flags = re.U)
##    speech = re.sub(u'([!?.]) — ([а-яё]+?)', u'\1— \2', ohne_abbrev, flags = re.U)
##    sentences = re.findall(u'[А-ЯЁ].*? [.!?…] ', speech, flags = re.U)
##    for sent in sentences:
##        sent = re.sub(u'([^а-яё][А-ЯЁX])\.', u'\1 \.', sent, flags = re.U)
##        sent = re.sub(u'([а-яё]+?)\. ([а-яё]+?)', u'\1 \. \2', sent, flags = re.U)
##        sent = re.sub(u'([!?.])— ([а-яё]+?)', u'\1 — \2', sent, flags = re.U)
##        sent = re.sub(u'ѫ', u',', sent, flags = re.U)
##        sent = re.sub(u'ω', u':', sent, flags = re.U)
##        sent = re.sub(u'…', u'...', sent, flags = re.U)
##        sent = re.sub(u'ѹ', u'/', sent, flags = re.U)
##        sent = re.sub(u'Ω', u'?', sent, flags = re.U)
##        sent = re.sub(u'ѧ', u'.', sent, flags = re.U)
##        arr_sent.append(sent)
##    w = codecs.open('sentences.txt', 'a', 'utf-8')
##    for sentence in arr_sent:
##        w.write(sentence + '\r\n')
##    w.close
##    return arr_sent

##def list_tokens(arr_sent):
##    arr_tokens = []
##    for sent in arr_sent:
##        tokens = sent.split(' ')
##        for token in tokens:
##            arr_tokens.append(token)
##    w = codecs.open('tokens.txt', 'a', 'utf-8')
##    for token in arr_tokens:
##        w.write(token + '\r\n')
##    w.close
    

