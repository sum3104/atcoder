# -*- coding: utf-8 -*-
n = int(input())
count = 0
sequence = list(map(int, input().split()))

while all(a % 2 == 0 for a in sequence):
    sequence = [a/2 for a in sequence]
    count += 1
print(count)
