#AC

n = int(input())
a = list(map(int, input().split()))

tmp = a[0]

for i in range(1,n):
    if a[i] != tmp:
        print('No')
        break

    tmp = a[i]

    if i == n-1:
        print('Yes')



