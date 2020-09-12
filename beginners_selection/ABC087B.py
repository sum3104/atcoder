# -*- coding: utf-8 -*-
a, b, c, x = [int(input()) for _ in range(4)]
ans = 0
# for _ in range(n)は0からn未満までの範囲が対象→n回までやる場合n + 1
# 変数をアンダーバーにするのは、その変数を使っていない事を表現するpythonの慣習
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500 * i + 100 * j + 50 * k == x:
                ans += 1
print(ans)
