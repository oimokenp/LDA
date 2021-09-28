# LDA
## 実行順番
seliarizecorpus.py -> coherence.py -> LDA_csv.pyの順に実行してください．

コーパスの作成，トピック数の決定，LDAの結果をCSVファイルに出力するファイルに分かれている．

# LDAの評価指標
- perplexity: モデルの予測精度の評価指標
- coherence: トピックの品質を測る評価指標
この指標を基にトピック数を決めます．
Perplexityは低い数値、Coherenceは高い数値が良いとされていますが，テキストデータによっては役に立たない場合があるので，
参考程度にしてください．

## ファイルの特徴
- Seliarizecorpus.py
入力するのはテキストファイルで、1行1文書(1行1ツイート)にしています。
入力ファイルをcsvにするなら自分でやってね ストップワードでは、1行一単語です。 

- Coherence.py
先ほど作ったdictとmmの名前に変えて実行 

- LDA_csv.py
トピック数の数字変えてdict,mm変えて実行
