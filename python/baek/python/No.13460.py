dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def is_valid(r, c):
    return 1 <= r < N - 1 or 1 <= c < M - 1


def find_min(r, c, cnt):
    global result

    if cnt == 10:
        if result > cnt:
            result = cnt
            return

    if cnt >= result:
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        while is_valid(nr, nc) and arr[nr][nc] != "B" and arr[nr][nc] != "R" and arr[nr][nc] != "O":
            nr += dr[i]
            nc += dc[i]

        nr -= dr[i]
        nc -= dc[i]
        if arr[nr][nc] == "O":
            cnt += 1
            if cnt < result:
                result = cnt
                return
        elif arr[nr][nc] == "B" or arr[nr][nc] == "R":
            arr[r][c], arr[nr - dr[i]][nr - dc[i]] = arr[nr - dr[i]][nr - dc[i]], arr[r][c]
            find_min(nr - dr[i], nr - dc[i], cnt + 1)
            arr[r][c], arr[nr - dr[i]][nr - dc[i]] = arr[nr - dr[i]][nr - dc[i]], arr[r][c]
        else:
            arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
            find_min(nr, nc, cnt + 1)
            arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
red_idx = [0, 0]
blue_idx = [0, 0]
whole_idx = [0, 0]
visited = [[0] * N for _ in range(M)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            red_idx[0], red_idx[1] = i, j
        if arr[i][j] == "B":
            blue_idx[0], blue_idx[1] = i, j
        if arr[i][j] == "O":
            whole_idx[0], whole_idx[1] = i, j

result = 11

find_min(red_idx[0], red_idx[1], 0)


print(result)
