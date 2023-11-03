#https://atcoder.jp/contests/abc032/tasks/abc032_c
N, K = map(int, input().split())
s = []
for i in range(N):
    s.append(int(input()))
print(N, K, s)


right = 0
tmp = 1
ans = 0

# 入力に0があったらK以下になるのが確定だからN返す
if 0 in s:
    print(N)

else:
    for left in range(N):
        #条件を満たす間はrightをスライド
        while right < N and K >= tmp*s[right]:

            tmp *= s[right]
            right += 1

        ans = max(ans, right-left)

        # 条件を満たさないときはleftをスライドして考慮されなくなる
        # 数値を除いておく

        # leftとrightが一緒の場合両方同時にスライド
        if left == right:
            right += 1

        else:
            tmp //= s[left]

    print(ans)
                              
                

