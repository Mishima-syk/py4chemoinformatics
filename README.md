# 目次
ちょっと追加した(2018.12.12)。web interfaceは入門の範囲を超えそうなのでどうするかは考える。

- [AsciiDoc Syntax Quick Reference](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#formatted-text)

<img src="python_for_ci.png" width="250" />

## [01 はじめに](ch01_introduction.asciidoc)
- ケモインフォマティクスとは？

## [02 ケモインフォマティクスのための環境を整えよう](ch02_installation.asciidoc)
- Anaconda(Python, Jupyter, scikit-learn)
- RDKit

## 03 Pythonプログラミングの基礎
- Pythonの基礎（必要だったら）
- Jupyter notebookで便利に使おう

## 04 ケモインフォマティクスのための公開データベース
- ChEMBL
- PubChem

## [05 RDKitで構造情報を取り扱う](ch05_rdkit.asciidoc)
- SMILESとは？
- 構造を描画してみよう
- 複数の化合物を一度に取り扱うには？

## 06 化合物の類似性を評価してみる
- 記述子、フィンガープリント
- 類似度を計算する

## 07 沢山の化合物を一度にみたい
- Chemical Spaceとは
- tSNEをつかったマッピング
- 主要な骨格による分類(MCS)
- Matched Molecular Pairによる化合物ネットワーク

## 08 構造活性相関（QSAR）の基礎
- 効果ありなしの原因を考えてみる（分類問題）
- 薬の効き目を予測しよう（回帰問題）
- R分解とFree wilson analysis
- モデルの適用範囲(applicability domain)

## 09 ディープラーニング入門
- TensorFlowとKerasについて
- Google colab(ずっとフリーかわからないので要検討)
- インストールしてみよう

## 10 ディープラーニングを利用した構造活性相関
- 記述子を工夫してみる(neural fingerprint)
- DNNを利用した予測モデル構築

## 11 コンピューターに化学構造を考えさせる
- Recurrent Neural Networkを利用した構造生成
