'''
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
5 15
-8 4 6 -9 -1
-1 1 0 -2 10 10 0 2 5 2 10 7 -9 7 -8
11 20
3 -8 4 0 -1 -4 8 3 7 -3 1
3 10 0 1 10 0 -8 -6 9 -7 -1 1 -1 4 10 6 0 -8 -5 0
11 16
-6 0 -1 7 5 -1 -3 0 -9 8 4
0 -6 1 1 8 -8 0 -7 4 -7 -8 -2 1 4 0 -10
3 16
8 9 0
-4 9 -7 -1 -8 3 1 -6 -8 5 2 -7 -9 -10 8 9
11 3
3 -4 -7 7 -2 5 5 0 -2 -8 4
-1 1 3
14 6
-9 9 0 -7 8 10 7 -3 2 3 0 0 0 -2
8 1 -9 3 0 -7
17 10
-6 -1 -4 2 -5 1 -10 -9 8 -9 -6 1 10 0 -5 -8 1
7 6 2 7 -8 4 8 10 -2 9
11 9
8 6 -2 0 0 5 10 2 -10 -8 -10
10 -9 -7 -1 0 8 0 10 3

'''
# 두개의 숫자열
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))

    max_multiply = 0

    if N > M:
        for i in range(N - M + 1):
            current_multiply = 0
            for j in range(M):
                current_multiply += arr_n[i + j] * arr_m[j]

            if current_multiply > max_multiply:
                max_multiply = current_multiply
    else:
        for i in range(M - N + 1):
            current_multiply = 0
            for j in range(N):
                current_multiply += arr_n[j] * arr_m[i + j]

            if current_multiply > max_multiply:
                max_multiply = current_multiply

    print(f"#{tc} {max_multiply}")
