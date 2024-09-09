T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())

    result = 0

    if b < 2 or c < 3:
        print(f"#{tc} {-1}")
        continue

    if b >= c:
        result += b - (c - 1)
        b = c - 1

    if a >= b:
        result += a - (b - 1)
        a = b - 1

    print(f"#{tc} {result}")
