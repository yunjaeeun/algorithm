T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    result = ""
    while True:
        N *= 2
        if N == 1:
            result += "1"
            break

        if N < 1:
            result += "0"

        if N > 1:
            result += "1"
            N -= 1

        if len(result) == 13:
            result = "overflow"
            break

    print(f"#{tc} {result}")
