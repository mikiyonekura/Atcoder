#メジャーを伸ばしていくやつ
#区間がXを超えない場合メジャーを伸ばす

li = list(map(int, input().split()))
X = int(input())
N = len(li)

right, ans, measure = 0, 0, 0

for left in range(N):
    # print("left詰める","l:r",left,right,"m",measure)
    while right < N and measure+li[right] <= X:
        measure += li[right]
        right += 1
        # print("rightのびる","l:r",left,right,"m",measure)
    ans = max(ans, right-left)

    #leftがrightを追い越しちゃダメだから
    if left==right:
        right += 1
        continue
    measure -= li[left]
print(ans)