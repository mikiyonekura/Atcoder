n, x = map(int, input().split())
A = list(map(int, input().split()))

flag = 0

for a in A:
    if a == x:
        flag = 1

if flag:
    print('Yes')
else:
    print('No')