n, x = map(int, input().split())
s = str(input())


def calc(point, flg):
    if flg:
        point += 1
    else:
        if point > 0:
            point -= 1
    return point


for i in s:
    if i == 'o':
        x = calc(x, True)
    elif i == 'x':
        x = calc(x, False)

print(x)
