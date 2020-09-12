n = input()
# 1, 2, 3, 4, 5...をリストに変換する方法
lst = list(map(int, input().split()))

answer = 0
tmp = 0
isFirst = True

for i in lst:
    if isFirst:
        isFirst = False
        tmp = i
    else:
        if tmp > i:
            answer += tmp - i
        else:
            tmp = i
print(answer)
