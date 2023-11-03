n = int(input())
h = list(map(int, input().split()))

# 初期化
# 最小化のため最大値で初期化
dp = [10**5+1] * n

# 初期条件
# 柱0の移動コストは0
# 柱1への最小コストは柱0からの場合のみ
dp[0] = 0
dp[1] = abs(h[1]-h[0])

# 解を求めるまで繰り返す
for i in range(2, n):
    # dpテーブルの解を利用して解を求める
    # 柱iまでの最小コストは柱i-1からの移動か柱i-2からの移動の小さい方
    dp[i] = min(abs(h[i]-h[i-1])+dp[i-1], abs(h[i]-h[i-2])+dp[i-2])

print(dp[-1])
