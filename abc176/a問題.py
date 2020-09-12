n, x, t = map(int, input().split())
# (-(-n // x)): n / xの商（整数に切り上げ）
result = (-(-n // x)) * t
print(result)
