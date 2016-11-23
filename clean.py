# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk
nltk.data.path.append('/home/huhao/Data/nltk_data')
from nltk.corpus import stopwords
import re

stop = stopwords.words('english')
# punctuation_data = [',', '.', '!', '?', "'", '"', '(', ')', ':', ';', '-', '–']
pattern = re.compile(r'\s{2,}')
pattern_number = re.compile(r'\d+')
pattern_not_letter = re.compile(r'[^A-Za-z ]')

def clean_doc(doc_raw):
    # for t in punctuation_data:
    #     doc_raw = doc_raw.replace(t, '')
    # doc_raw = pattern_number.sub('', doc_raw)
    doc_raw = pattern_not_letter.sub('', doc_raw)
    list_doc_raw = doc_raw.split(' ')
    list_doc_raw = [w for w in list_doc_raw if w not in stop and len(w) != 0]
    # for t in stop:
    #     doc_raw = doc_raw.replace(t, '')
    # doc = pattern.sub(' ', doc_raw)
    doc = ''
    for w in list_doc_raw:
        doc += ' ' + w
    doc = doc[1:]
    return doc

def assembel(path):
    fp = open('WestburyLab.wikicorp.201004_sample_cleaned.txt', 'w')
    doc = ''
    for line in open(path):
        line = line.strip()
        if line != "---END.OF.DOCUMENT---":
            doc += ' ' + line
        else:
            doc = clean_doc(doc)
            fp.write(doc + '\n')
            doc = ''
    fp.close()

if __name__ == '__main__':
    assembel('WestburyLab.wikicorp.201004_sample.txt')