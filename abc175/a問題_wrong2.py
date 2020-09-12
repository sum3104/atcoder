# WR3
s = input()
lst = list(s)
counter = 0
buffer = 0
if 'R' not in lst:
    print(0)
else:
    for i in range(len(lst) - 1):
        if lst[i] == 'R':
            buffer += 1
        else:
            counter = buffer
            buffer = 0
        if buffer > counter:
            counter = buffer
    print(counter)
