a, b, c, d = map(int, input().split())

flg1 = a <= c <= b <= d
flg2 = c <= a <= d <= b
flg3 = a <= c <= d <= b
flg4 = c <= a <= b <= d
flg = flg1 or flg2 or flg3 or flg4

if flg:
    print('Yes')
else:
    print('No')
