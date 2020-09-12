n = input()
# 各桁の数字の和を求める方法
result = sum(list(map(int, str(n))))
if result == 0 or (result % 9) == 0:
    print('Yes')
else:
    print('No')
