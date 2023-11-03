n, k = map(int, input().split())
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
    # 柱iまでの最小コストは柱i-1, ... ,柱i-kからの移動の中で最も小さいもの
    dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    for j in range(2, k+1):
        if i - j >= 0:
            dp[i] = min(abs(h[i]-h[i-j])+dp[i-j], dp[i])

print(dp)
print(dp[-1])