n = int(input())
cnt = 0

for i in range(1, n + 1):
    dnum = str(i)
    onum = str(oct(i))[2:]
    numStr = dnum + onum
    lst = list(numStr)
    lst_unique = list(set(lst))

    if not '7' in lst_unique:
        cnt += 1

print(cnt)
