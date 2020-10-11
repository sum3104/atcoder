n = input()
lst = list(map(int, input().split()))

s = sorted(lst)

mx = max(s)
mn = min(s)

while mx != mn:
    s_replace = [i - mn if i == mx else i for i in s]
    s = s_replace
    mx = max(s_replace)
    mn = min(s_replace)

print(mx)
