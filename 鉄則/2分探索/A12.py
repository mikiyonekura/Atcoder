#イメージ(単調増加する配列)
#答えの範囲：x_i = 1...10**9秒
#答えを2部探索していき条件を満たす範囲を探す: k = f(x_i)
#k = [f(x_1), f(x_2), f(x_3), f(x_4), f(x_5)]
#k = [2,4,6,8,10]

# もしx = 45**9秒(mid), k(45**9) = 300 (目的のk = 400)
# 超えてないから配列の左側(r = mid)にある



n, k = map(int,input().split())
A = list(map(int,input().split()))

#可能性のある答えを元に2部探索する
#Aの範囲：10**9秒まで

def check(mid,A,k):
    sum = 0
    for a in A:
        sum += mid // a

    if sum >= k:
        return 1
    else:
        return 0


#2部探索
l = 1
r = 10**9


#答えがmid秒の時 <k かどうか調べる

while l < r:
    mid = (l+r) // 2
    flag = check(mid,A,k)
    if flag:
        r = mid
    else:
        l = mid + 1

print(l)

