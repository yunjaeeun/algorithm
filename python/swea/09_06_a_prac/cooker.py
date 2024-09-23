T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000

    for i in range(1, N):
        num = arr[0][i] + arr[i][0]
        for j in range(N):
            if j != i and j != 1:
                for k in range(N):
                    if j != k:
                        num_2 = arr[j][k] + arr[k][j]

                if abs(num - num_2) < result:
                    result = abs(num - num_2)

    print(f"#{tc} {result}")
