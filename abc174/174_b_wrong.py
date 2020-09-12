# -*- coding: utf-8 -*-
import math
# 標準入力
# 入力回数をn, 原点からの距離をdとして取得する
n, d = map(int, input().split())

# 標準入力から複数行に渡って絶対値を取得する
xy = [map(int, input().split()) for _ in range(n)]
count = 0
for j in xy:
    x, y = [list(abs(j)) for i in zip(*xy)]
    if math.sqrt(x**2 + y**2) <= d:
        count = count + 1
print(count)