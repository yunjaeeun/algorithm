T = int(input())

N, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0]
dj = [0, 1]

for i in range(N):
    for j in range(N):
        ni = j + di[0]
        nj = i + dj[0]
        now = arr[j][i]
        now_len = 0
        while 0 <= ni < N and 0 <= nj < N:
            if now != arr[ni][nj] and now_len != X:

