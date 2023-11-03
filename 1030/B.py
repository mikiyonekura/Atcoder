n = int(input())

for i in range(n,920):
    a = i // 100
    b = (i % 100) // 10
    c = i % 10

    if a*b == c:
        print(i)
        break
