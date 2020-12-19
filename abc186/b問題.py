import itertools

h, w = map(int, input().split())
l2d = [input().split() for _ in range(h)]

lst = list(itertools.chain.from_iterable(l2d))
lst = [int(i) for i in lst]

minValue = min(lst)
ans = 0

for i in lst:
    if i > minValue:
        ans = ans + (i - minValue)

print(ans)
