n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a, reverse=True)

alice = 0
bob = 0
flg = True

for i in a_sorted:
    if flg:
        alice += i
    else:
        bob += i
    flg = not flg

print(alice - bob)
