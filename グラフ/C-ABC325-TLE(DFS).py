#DFSみたいに再帰でやったらTLEなった
# https://atcoder.jp/contests/abc325/tasks

import sys
sys.setrecursionlimit(10**6)  # 再帰の深さの制限を増やす

H,W = map(int, input().split())

field = []
for i in range(H):
    row = list(input())
    field.append(row)

direc = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

def dfs(h,w):

    field[h][w] = "-"

    for d in direc:
        next_h = h+d[0]
        next_w = w+d[1]
        if next_h >= H or next_w >= W:
            continue
        if next_h < 0 or next_w < 0:
            continue
        next_point = field[next_h][next_w]

        if next_point == ".":
            continue
        if next_point == "-":
            continue
        # if next_point == "#":
            
        dfs(next_h,next_w)


count = 0
for h in range(H):
    for w in range(W):
        # print(h,w)
        if field[h][w]=='#':
            # print('start')
            # field_print(field)
            dfs(h,w)
            # print('fin')
            # field_print(field)
            count += 1

print(count)

