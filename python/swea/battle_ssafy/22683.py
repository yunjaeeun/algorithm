di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def find_root(r, c, father, cnt, status):
    global result
    if result != -1 and cnt >= result:
        return

    if arr[r][c] == "Y":
        if result == -1:
            result = cnt
            return
        else:
            if result > cnt:
                result = cnt
            return

    for i in range(4):
        nr, nc = r + di[i], c + dj[i]
        if is_valid(nr, nc) and visited[nr][nc] != 1:
            if arr[nr][nc] == "G" or arr[nr][nc] == "Y":
                visited[nr][nc] = 1
                find_root(nr, nc, father, cnt + 1)
                visited[nr][nc] = 0
            elif arr[nr][nc] == "T" and father > 0:
                # arr[nr][nc] = "."
                visited[nr][nc] = 1
                find_root(nr, nc, father - 1, cnt + 1)
                # arr[nr][nc] = "T"
                visited[nr][nc] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = [0, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "X":
                start[0], start[1] = i, j
                visited[i][j] = 1
                break
    result = -1
    find_root(start[0], start[1], K, 0, "UP")
    print(f"#{tc} {result}")
