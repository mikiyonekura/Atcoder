n, t = map(str,input().split())
n = int(n)
s = []
for i in range(n):
    s.append(input())

# print(n,t,s)

def compare(s, t):

    # 1文字も変わっていない
    if s == t:
        return True
    # 1文字削除
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[:i] + s[i+1:] == t:
                return True
    # 1文字挿入
    elif len(s) - 1 == len(t):
        for i in range(len(t)):
            if s[:i] + s[i+1:] == t:
                return True
    # 1文字変更
    elif len(s) == len(t):
        diff = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                diff += 1
            if diff > 1:
                return False
        if diff == 1:
            return True
    return False

lists = []
for i in range(n):
    #s[i]とtを比較
    isOK = compare(s[i], t)
    # print(f'比較:{s[i],t}')
    # print(isOK)
    if isOK == 1:
        lists.append(i+1)

# print(lists)

if len(lists) == 0:
    print(0)

else:
    ans = " ".join(map(str, lists))
    print(len(lists))
    print(ans)




