# Beam Search NLP

## Beam Search

条件付き確率場とも考えられる単語の連なりから、ネットワークの探索範囲を限定することでそれなりの良い答えを得る方法。  

<div align="center">
  <img width="750px" src="https://user-images.githubusercontent.com/4949982/49210846-77fcc900-f401-11e8-920f-3341bca0837b.png">
</div>
<div align="center"> 図1. 幅2の探索例 </div>


難しいのは、単語同士の関連する確率の表現で、できるだけながい語を見るほうが望ましいというネットワークの結合の重要度を与える必要がある。  

# 処理フロー

## 分かち書き
```console
$ python3 10-tokenize.py 
```

## 条件付き確率場の生成
```console
$ python3 20-term_chaine.py
```

## DBの結合
```console
$ python3 30-scan_level_db.py
```

## DBの内容の書き出し
```console
$ python3 40-dump_level.py
```

## pythonのデータタイプに変換
```console
$ python3 50-make_term_term_freq.py
```

## 探索
単純にビーム数4でやるとそれなりに安定したそれっぽい言葉の連なりが得られます

例:
```
```

## 時々ノイズを入れる
例1:
```
飯室 09 : 00 -1 8 ： 00 ） ・ 「 イイ 歳 」 「 オマエラ 」 「 イヤガラセ 」 など カタカナ表記 を しばしば 使う ・ ～～、 ーー 等 と 伸ばす こと が 多い 。 だから 、 
この 分野 の 話 は し ない と 、 この 人 は 、 貴方 が とても 大切 だ けど 、 それ が 「 刑事裁判 」 という もの で は なく て も 良い と 思っ た 。 でも 今 まで に 
```
例2:
```
ホリケンサイズ で は なく 、 その 人 は 「 自分 が 正しい と は 思わ なかっ たろ う に … こいつ を 産み 育て た 女性 は 「 私 の 言う 事 に なり まし たら 幸い で ある 、 と いう か … 。 まあ 、 俺 は リッカ を 抱き 寄せ て 、 それ が 何 ？ 」 と 聞い て <EOS>
```
例3:
```
コレラ に なっ て た の は 俺 の もの だ 。 それ が 、 今 は どう なっ た ん だろ ？ それ が 出来 ない の は なぜ な の ？ 」 って 言わ ない で くれ よ 。 <EOS>
```
例4:
```
アースイーター を 見 た 。 その 時 の 喜び が 味わえる グッズ 多数 揃え て おり ます が 、 これ は 、 家族 に 迷惑 が 掛かる から ね 。 <EOS>
```


