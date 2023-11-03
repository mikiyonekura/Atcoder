n, m = map(int,input().split())
A = list(map(int,input().split()))

from collections import defaultdict
d = defaultdict(int)

#累積和を計算しておく
d[0] = 0

for i in range(n):
    d[A[i]] += 1

k = sorted(d.items())
k = dict((x, y) for x, y in k)

for key, val in k.items():

    # 前のキーを計算する
    prev_key = key - 1
    
    # 前のキーが辞書に存在する場合にのみ、値を加算する
    if prev_key in k:
        k[key] += k[prev_key]

print(k)
ans = 0
for i in range(n):
    print(i)
    num = k[i+m] - k[i]
    ans = max(ans,num)

print(ans)