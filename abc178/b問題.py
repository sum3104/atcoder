a, b, c, d = map(int, input().split())

ab = [a, b]
cd = [c, d]
lst = []

for i in ab:
    for j in cd:
        lst.append(i * j)

print(max(lst))
