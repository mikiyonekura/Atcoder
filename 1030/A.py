x, y = map(int,input().split())

dif = abs(x-y)
#くだり
if x > y and dif < 4:
    print('Yes')

elif x < y and dif < 3:
    print('Yes')

else:
    print('No')