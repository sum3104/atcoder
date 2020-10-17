import math

n = int(input())
lst = list(map(int, input().split()))
absLst = list(map(lambda x: abs(x), lst))
sqrLst = list(map(lambda x: x * x, absLst))

m = sum(absLst)
e = math.sqrt(sum(sqrLst))
c = max(list(absLst))

print(m)
print(e)
print(c)
