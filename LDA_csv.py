# coding=utf-8

import logging
import os
import csv

import gensim

from toolz import frequencies
from gensim import corpora, models


# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
TOPIC_NUM = 10
name = 'xxxx'

#コーパス・辞書の読み込み
corpus = corpora.MmCorpus('../corpus/{0}_corpus.mm'.format(name))
dictionary = corpora.Dictionary.load('../corpusdict/{0}_dict.dict'.format(name))

#LDAのモデル作成
lda = models.ldamodel.LdaModel(corpus = corpus, num_topics = TOPIC_NUM, id2word = dictionary, random_state = 1)

with open('../csv/LDA_jumanpp_{0}.csv'.format(name), 'w', encoding = 'sjis') as f:
  writer = csv.writer(f)
  for topic in lda.show_topics(-1):
    #print(topic)
    writer.writerow(topic)

with open('../csv/topic_per{0}.csv'.format(name), 'w', encoding = 'sjis') as f:
  writer = csv.writer(f)
  for topics_per_document in lda[corpus]:
    #print(topics_per_document)
    writer.writerow(topics_per_document)
