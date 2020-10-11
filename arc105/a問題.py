a, b, c, d = map(int, input().split())
lst = [a, b, c, d]
s = sorted(lst)
flg = False

if a == b == c == d:
    flg = True
if s[0] + s[3] == s[1] + s[2]:
    flg = True
if s[0] + s[1] + s[2] == s[3]:
    flg = True

if flg:
    print('Yes')
else:
    print('No')
