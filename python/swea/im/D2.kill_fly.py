'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

'''

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            type_1 = arr[i][j]
            type_2 = arr[i][j]

            for k in range(1, M):
                if i + k < N:
                    type_1 += arr[i + k][j]
                if j + k < N:
                    type_1 += arr[i][j + k]
                if i - k >= 0:
                    type_1 += arr[i - k][j]
                if j - k >= 0:
                    type_1 += arr[i][j - k]
                if i + k < N and j + k < N:
                    type_2 += arr[i + k][j + k]
                if 0 <= i - k and 0 <= j - k:
                    type_2 += arr[i - k][j - k]
                if 0 <= i - k and j + k < N:
                    type_2 += arr[i - k][j + k]
                if i + k < N and 0 <= j + k:
                    type_2 += arr[i + k][j - k]
            max_type = max(type_1, type_2)
            if result < max_type:
                result = max_type

    print(f"#{tc} {result}")
