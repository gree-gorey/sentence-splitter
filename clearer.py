# -*- coding: utf-8 -*-
import lxml.html
import lxml.etree
import re
import xml.sax.saxutils
import codecs


def gi(name):
    text = u''
    ft = codecs.open(name, 'r', 'utf-8')
    for line in ft:
        line = line.rstrip()
        line = xml.sax.saxutils.escape(line)
        if line[0:3] == u'   ':
            text += u'\r\n'
        try:
            if line[0] != u' ':
                text += u' '
        except:
            continue
        text += line
    return text


def clear(text):
    text = text.replace(u'--', u'—')
    text = re.sub(u'([а-яА-ЯЁё])——?([а-яА-ЯЁё])', u'\\1-\\2', text)
    text = re.sub(u'([а-яА-ЯЁё])――?([а-яА-ЯЁё])', u'\\1-\\2', text)
    text = re.sub(u' +', u' ', text)
    text = re.sub(u'([A-Za-z0-9@])\.([A-Za-z0-9@])', u'\\1ѧ\\2', text)
    text = re.sub(u'([A-Za-z0-9@])//([A-Z:a-z0-9@])', u'\\1ꙋꙋ\\2', text)
    text = re.sub(u'([A-Za-z0-9@])/([A-Z:a-z0-9@])', u'\\1ꙋ\\2', text)
    text = re.sub(u'([A-Za-z]):([A-Za-z0-9@/])', u'\\1ω\\2', text)
    text = re.sub(u'([A-Za-z0-9@])\?([A-Za-z0-9@])', u'\\1Ω\\2', text)
    text = re.sub(u'([0-9]),([0-9])', u'\\1ѫ\\2', text)
    text = re.sub(u'([:;№§\(,\.\?\|!\)—])', u' \\1 ', text)
    text = text.replace(u' - ', u' — ')
    text = text.replace(u'- ', u' — ')
    text = text.replace(u' -', u' — ')
    text = text.replace(u' ― ', u' — ')
    text = text.replace(u' ―', u' — ')
    text = text.replace(u'― ', u' — ')
    text = text.replace(u' —', u' — ')
    text = text.replace(u'— ', u' — ')
    text = re.sub(u'[«»„““”‘’]', u'"', text)
    text = re.sub(u'"+', u'"', text)
    text = re.sub(u'"', u' " ', text)
    text = re.sub(u' +', u' ', text)
    text = text.replace(u'. . .', u'…')
    text = text.replace(u'! ?', u'?!')
    text = text.replace(u'\r\n ', u'\r\n')
    return text


with codecs.open(u'test.txt', u'r', u'utf-8') as f:
    a = f.read()

a = clear(a)

with codecs.open(u'output.txt', u'w', u'utf-8') as w:
    w.write(a)

# text = gi(u'harms.txt') + u'\r\n' + gi(u'lipavski.txt')
# text = clear(text)
# ft = codecs.open(u'podcorpus_Sasha_Grisha_Tanya.txt', 'w', 'utf-8')
# # print text
# ft.write(text)
# # print text
# text = clear(u'морж!рука 66,7 &amp бело—красный и "45 про"шпорап)арп -- «dsf»: http.g8.9om 77.9 fghj - hg ( ghjkj) держать.как-то http://vk.com/im?sel=c43 "Не тяжело?"  --  спросил его маленький человек.-- "Нет,ничего",- говорит длинный.')
# text = xml.sax.saxutils.escape(text)
# #print text
# fn = codecs.open(u'test_v2_1.txt', 'r', 'utf-8')
# text2 = fn.read()
# print clear(text2)