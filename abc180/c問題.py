# 約数を求める関数 O(root n)
def get_divisors(n):
    if n < 1:
        return
    i = 1
    while i * i <= n:
        if n % i == 0:
            yield i
            if i * i != n:
                yield round(n / i)
        i = i + 1


x = int(input())
lst = []
for item in get_divisors(x):
    lst.append(item)

sortedLst = sorted(lst)

for _ in sortedLst:
    print(_)
