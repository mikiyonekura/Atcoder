n, s = map(int, input().split())
A = list(map(int, input().split()))

#純粋にbit全探索
#今回はN=60だから使えない

# for bit in range(1<<n):
#     ans = 0

#     for i in range(n):
#         if bit & 1<<i:
#             ans += A[i]

#     if ans == s:
#         print('Yes')
#         exit()

#DPでとく
#n✖️sの行列で解ける
#dp[n][s]: n枚のカードを使ってsが作れるか？
#dp[n-1][s]がTrueなら dp[n][s]もTrue
#dp[n-1][s-A[n]]がTrueの場合も dp[n][s]はTrue

dp = []
print(s)
firstLow = [1] + [0] * s
dp.append(firstLow)

print(dp)