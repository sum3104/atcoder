n = int(input())

a = 1
b = 1
num1 = 3
num2 = 5
flg = False

while num1 < n:
    m = n - num1
    b = 1
    num2 = 5
    if m % 5 == 0:
        while num2 <= m:
            if num2 == m:
                flg = True
                break
            b += 1
            num2 = 5 ** b
    a += 1
    num1 = 3 ** a

# ctrl + / : comment out
# 3 + 5 ** m となるもう一つのパターンが必要
# このまま書くとTLEになる
# if not flg:
#     a = 1
#     b = 1
#     num1 = 3
#     num2 = 5
#
#     while num2 < n:
#         m = n - num2
#         a = 1
#         num1 = 3
#         if m % 3 == 0:
#             while num1 <= m:
#                 if num1 == m:
#                     flg = True
#                     break
#                 a += 1
#                 num1 = 3 ** a
#             b += 1
#             num2 = 5 ** b

if flg:
    print(str(a - 1) + ' ' + str(b))
else:
    print('-1')
