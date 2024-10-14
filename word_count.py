from collections import defaultdict # collections モジュールから defaultdict クラスをインポートするための構文

# Map関数: テキストを単語ごとに分割して、(単語, 1) のペアを生成
def map_function(text):
    words = text.split()
    word_count = []
    for word in words:
        word_count.append((word, 1))
    return word_count

# Reduce関数: 同じ単語を集約して、出現回数を数える
def reduce_function(mapped_data):
    reduced_data = defaultdict(int)
    for word, count in mapped_data:
        reduced_data[word] += count
    return reduced_data

# サンプルテキスト
text_data = [
    "map reduce is powerful",
    "map reduce is useful",
    "python map reduce example"
]

# Mapフェーズ: 各テキストデータに対してMap関数を適用
mapped = []
for text in text_data:
    mapped.extend(map_function(text))

# Reduceフェーズ: 同じキー（単語）に対してReduce関数を適用
reduced = reduce_function(mapped)

# 結果を表示
for word, count in reduced.items():
    print(f"{word}: {count}")
