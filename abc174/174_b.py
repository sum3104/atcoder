# -*- coding: utf-8 -*-
# 1行の入力を受け取って分割して代入？
n, d = map(int, input().split())

result = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x * x + y * y <= d * d:
        result += 1
print(result)