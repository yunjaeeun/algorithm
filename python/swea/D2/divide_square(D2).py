T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    square_len = N ** (1/2)

    if square_len % 1 == 0:
        print(f"#{tc} {int(square_len)}")
    else:
        print(f"#{tc} 0")
