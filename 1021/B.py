n = int(input())

w = []
x = []

for i in range(n):
    wTmp, xTmp = map(int, input().split())
    w.append(wTmp)
    x.append(xTmp)

numAttendList = []
for t in range(1,24):
    numAttend = 0
    for i in range(n):

        if x[i]+t > 24:
            time = x[i]+t - 24
        else:
            time = x[i]+t

        if 9 <= time <= 17:
           numAttend += w[i]

    numAttendList.append(numAttend)

print(max(numAttendList))




