h, w = map(int, input().split())
s = [input().split() for _ in range(h)]

counter = 0
v = []
vc = 0

# print(s)
# [['..#'], ['#..']]

# print(str(s[0])[1:-1])
# '..#'

# 行列変換したリスト作成
for i in range(w):
    vertical = ''
    for j in s:
        work = str(j[0])
        vertical += work[vc]
    v.append(vertical)
    vc += 1

# パターン数の取得
for i in s:
    work = str(i)[1:-1]
    memo = ''
    for j in work:
        if memo == '.' and j == '.':
            counter += 1
        memo = j

for i in v:
    work = str(i)
    memo = ''
    for j in work:
        if memo == '.' and j == '.':
            counter += 1
        memo = j

print(counter)

# もうちょい整ったコードにした方がよさみ
