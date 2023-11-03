n, q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []

for _ in range(q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# print(n,q,A,L,R)

for i in range(q):
    # print(f'{L[i]}日目から{R[i]}日目までの合計来場者数')
    
    ans = 0
    for j in range(L[i]-1,R[i]):
        ans += A[j]

    print(ans)
