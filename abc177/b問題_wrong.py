s = input()
t = input()
flg = False

if t in s:
    print(0)
else:
    def recursive_find(target, find):
        if len(find) == 1:
            return ''
        sliced = find[:-1]
        if sliced in target:
            return sliced
        else:
            recursive_find(target, sliced)

    result = recursive_find(s, t)
    if result is None:
        result = ''

    # 後ろ1文字だけにマッチするパターン
    chr_final = t[-1:]
    if chr_final in s:
        if s.find(chr_final) == len(t) - 1:
            flg = True

    if flg:
        print(len(t) - 1)
    else:
        count = len(t) - len(result)
        if count == 0:
            count = len(t)
        print(count)
