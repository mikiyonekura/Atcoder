n, q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []

for _ in range(q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# print(n,q,A,L,R)

# 累積和を計算しておく
# l=1日目からr日目を計算するときlist[r]-list[l-1]
# l-1のためにlist[0]=0を追加しておく
accumList = [0]
accum = 0
for a in A:
    accum += a
    accumList.append(accum)

for i in range(q):
    # print(f'{L[i]}日目から{R[i]}日目までの合計来場者数')
    
    ans = accumList[R[i]] - accumList[L[i]-1]

    print(ans)
