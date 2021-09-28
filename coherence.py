# coding=utf-8

import logging
import os

import gensim
import numpy as np

from toolz import frequencies
from gensim import corpora, models
from gensim.models.ldamodel import CoherenceModel

name = 'train'

#コーパス読み込み
corpus = corpora.MmCorpus('./corpus/{0}_corpus.mm'.format(name))

#辞書の読み込み
dictionary = corpora.Dictionary.load('./corpusdict/{0}_dict.dict'.format(name))

#Coherence, perplexityによりTOPIC数の決定のために1度回す
for i in range(1,51):
  lda = models.ldamodel.LdaModel(corpus = corpus, num_topics = i, id2word = dictionary, alpha = 0.01, random_state = 1)
  cm = CoherenceModel(model = lda, corpus = corpus, coherence = 'u_mass')
  coherence = cm.get_coherence()

  perwordbound = lda.log_perplexity(corpus)
  perplexity = np.exp2(-perwordbound)

  print(f"num_topics = {i}, coherence = {coherence}, perplexity = {perplexity}")