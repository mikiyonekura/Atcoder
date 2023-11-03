n, x = map(int,input().split())
A = list(map(int,input().split()))

#本来はソートが必要

def binarySearch(l,r):

    while l <= r:
        #左の添字＋右の添字/2で中央の添字
        #割り切れない場合は切り捨て
        mid = (l+r) // 2 

        #num is right side
        if A[mid] < x:
            l = mid + 1

        #num is left side
        if A[mid] > x:
            r = mid - 1

        #hit
        if A[mid] == x:
            return mid
        
    return -1

l = 0
r = n - 1

ans = binarySearch(l,r)
print(ans)

