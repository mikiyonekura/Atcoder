#TLE

n, t = map(str,input().split())
n = int(n)
s = []
for i in range(n):
    s.append(input())

# print(n,t,s)

def compare(s, t):

    isOK = 0
    a = 0
    b = 0
    c = 0
    d = 0

    distance = abs(len(s) - len(t))

    #１つ目の条件
    if s == t:
        a = 1

    else:
        if distance == 0 and len(s) == len(t):
            d = 1


    #２つ目
    if distance == 1 and len(s) < len(t):
        b = 1

    #３つ目
    if distance == 1 and len(s) > len(t):
        c = 


    #exa1
    if (a == 1 and b == 0 and c == 0 and d == 0) or (a == 0 and b == 1 and c == 0 and d == 0) or (a == 0 and b == 0 and c == 1 and d == 0) or (a == 0 and b == 0 and c == 0 and d == 1):
        isOK = 1

    return isOK

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




