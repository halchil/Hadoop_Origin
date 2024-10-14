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

# ワードの分割について

```
words = text.split()
word_count = []
```
text という変数に入っている文字列を split() メソッドを使って分割する。
split() のデフォルトの動作では、スペース（空白）を基準に文字列を分割し、単語ごとにリストに格納する。

例: `text = "Hello world"` なら、words は `["Hello", "world"]` というリストになる。

`word_count = [] `は、これは空のリストを作成しています