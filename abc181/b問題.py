# n
# a1 b1
# .....
# an bn

n = int(input())
total = 0

for i in range(n):
    a, b = map(int, input().split())
    length = b - a + 1
    if length == 0:
        total += (a + b) * length / 2
    else:
        total += (a + b) * (length - 1) / 2 + ((a + b) / 2)

print(int(total))
