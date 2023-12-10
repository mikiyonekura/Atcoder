#https://qiita.com/u2dayo/items/8c1601a61841540b4947
#めっちゃ基礎的なbit全探索の問題
#bit全探索はN=20くらいまでしか無理．それ以上は２次元のDPとかでとく．

n, m = map(int, input().split())
A = list(map(int, input().split()))

#bit全探索を実装

#1(２進数)を左にnbitシフトする．2**n回ループを回す．
for bit in range(1<<n):
    # 各組み合わせにおける和を計算する
    ans = 0
    # 各組み合わせにおいてどの桁が1になっているかを判定する
    for i in range(n):
        if bit & (1<<i):
            ans += A[i]
    if ans == m:
        print('Yes')
        exit()