n = int(input())
a = [int(input()) for _ in range(n)]

a_distinct = list(set(a))
count = 0

for i in a_distinct:
    count += 1

print(count)
