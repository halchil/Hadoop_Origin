# Basic Note

# collections モジュールの基本的な使い方

```
count = defaultdict(int)
```
のような使われ方をするが、defaultdictは辞書型である。(感覚的には変数に近い)
intはデフォルト(キーが何も入っていない場合の)型である。

keyとvalueの設定方法について
```
defaultdict(int)['apple'] = 1
```
`defaultdict(int)`に対して、そのまま右にkeyである`['apple']`を付け、`= 1`でvalueを設定する。
これで、countの中身が以下のように設定される。
```
{'apple': 1}
```
これを繰り返すと、countにkeyとvalueのセットが蓄積され、

```
{'apple': 1, 'banana': 1}
```
と増えていく。