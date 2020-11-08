import math

n = int(input())
lst = list(map(int, input().split()))

areAllSame = len(list(set(lst))) == 1
if areAllSame:
    print(lst[0])
    exit()

def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2:
        return False
    # 2は素数
    elif num == 2:
        return True
    # 偶数は素数ではない
    elif num % 2 == 0:
        return False

    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    # 素数
    return True


def callIsPrime(input_num=1000):
    numbers = []
    # ループしながら素数を検索する
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)

    # 素数配列を返す
    return numbers


maxNum = max(lst)
primeLst = callIsPrime(maxNum)
# あとで分かった気がする
# maxGcd = 0は存在しない
maxGcd = 1
ans = 0

for i in primeLst:
    gcd = 0
    for j in lst:
        if i > j:
            continue
        if j % i == 0:
            gcd += 1
    if gcd > maxGcd:
        maxGcd = gcd
        ans = i

print(ans)
