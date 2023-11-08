#Flog1のDPを復元することで最適経路を求める問題
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

ans = []
# 今回足場1...Nを0...n-1で表現してるから最後の足場はn-1
node = n - 1
# 最後のノードを追加
ans.append(node+1)

# 最初のノード(0の柱)に着くまで無限ループ
while True:
    if node == 0:
        break

    # 現在地まで辿り着くために1つ前の道をきたか否かを判断
    if dp[node-1] + abs(h[node]-h[node-1]) == dp[node]:
        # 1つ前に戻る
        node -= 1
    else:
        node -= 2

    # 現在地を追加
    ans.append(node+1)

# 最後のノードから入ってるから逆順にする必要がある
ans.reverse()
print(ans)


