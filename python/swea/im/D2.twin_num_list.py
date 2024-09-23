T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))

    result = 0

    if N > M:
        for i in range(N - M + 1):
            num = 0
            for j in range(M):
                num += arr_m[j] * arr_n[i + j]

            if i == 0:
                result = num
            elif num > result:
                result = num
    else:
        for i in range(M - N + 1):
            num = 0
            for j in range(N):
                num += arr_n[j] * arr_m[i + j]

            if i == 0:
                result = num
            elif num > result:
                result = num

    print(f"#{tc} {result}")
