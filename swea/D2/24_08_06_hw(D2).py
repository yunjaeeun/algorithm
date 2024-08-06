T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f"#{tc}")

    for i in range(N):
        result = ""
        for j in range(N):
            if arr[i][j] != 0:
                result += str(arr[i][j]) + " "
            else:
                break

        print(result)
