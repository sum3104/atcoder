x1, y1, x2, y2 = map(float, input().split())

if x1 < x2:
    x = x2 - x1
elif x1 > x2:
    x = x1 - x2

if y1 < y2:
    y = y2 - y1
elif y1 > y2:
    y = y1 - y2
elif y1 == y2:
    y = y1 * 2

a = y / x
if a > 0:
    b = y1 - (a * x1)
elif a < 0:
    b = y1 + (a * x1)

if b > 0:
    ans = -(a * x1)
elif b < 0:
    ans = a * x1
elif b == 0:
    ans = 0

print(ans)
