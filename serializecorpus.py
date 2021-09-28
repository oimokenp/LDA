# coding=utf8

import logging
import os

import gensim

from pyknp import Juman
from gensim import corpora, models

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

name = 'xxxx'
num = 0

#Jumanppオブジェクト
jumanpp = Juman()

if __name__ == '__main__':
  #トレーニングデータの読み込み
  #train_textsは2次元のリスト
  #テキストデータを1件ずつ分かち書き（名詞、形容詞、に限定）してtrain_textsに格納
  train_texts = []
  with open('../{0}.txt'.format(name), 'r', encoding = 'utf-8') as f:
    for lines in f:
      try:
        lines = lines.strip('\n')
        text = []
        result = jumanpp.analysis(lines)
        for mrph in result.mrph_list():
            if mrph.hinsi == '名詞' or mrph.hinsi == '形容詞':
                text.append(mrph.genkei)
            train_texts.append(text)
        print(num)
        num+=1
      except Exception as e:
        print(e)
        pass

  #辞書の作成・保存
  dictionary = corpora.Dictionary(train_texts)
  dictionary.save('../corpusdict/{0}_dict.dict'.format(name))

  #ストップワードの除外
  ignores = []
  ignored_words_file = '../stop_word.txt'
  with open(ignored_words_file, 'r') as f:
    ignores = [line.replace(os.linesep, "") for line in f]
  
  #フィルタリング
  dictionary.filter_extremes(no_below = 1, no_above = 0.6)
  stop_ids = [dictionary.token2id[ig] for ig in ignores if ig in dictionary.token2id]
  dictionary.filter_tokens(stop_ids)
  dictionary.compactify()

  #コーパス作成
  corpus = [dictionary.doc2bow(text) for text in train_texts]

  corpora.MmCorpus.serialize('../corpus/{0}_corpus.mm'.format(name), corpus)
