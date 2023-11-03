d = int(input())
n = int(input())
L = []
R = []

for _ in range(n):
    l, r = map(int,input().split())
    L.append(l)
    R.append(r)

accumList = [0]*(d+2)

for i in range(n):
    accumList[L[i]] += 1
    accumList[R[i]+1] += -1

tmp = 0
for i in range(d+1):
    accumList[i] += tmp
    tmp = accumList[i]

for ans in accumList[1:-1]:
    print(ans)