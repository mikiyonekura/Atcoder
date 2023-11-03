#再帰を使わない方法
H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]

direc = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def sensor(start_h, start_w):
    stack = [(start_h, start_w)]
    
    while stack:
        h, w = stack.pop()
        if not (0 <= h < H) or not (0 <= w < W) or field[h][w] != "#":
            continue
        
        field[h][w] = "-"
        for dh, dw in direc:
            next_h, next_w = h + dh, w + dw
            stack.append((next_h, next_w))

count = 0
for h in range(H):
    for w in range(W):
        if field[h][w] == '#':
            sensor(h, w)
            count += 1

print(count)

