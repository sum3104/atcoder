s = input()
counter = 1
buffer = 0
if 'R' not in s:
    print(0)
else:
    for i in range(len(s)):
        if s[i] == 'R':
            buffer += 1
        else:
            if buffer > counter:
                counter = buffer
            buffer = 0
        if buffer > counter:
            counter = buffer
    print(counter)
