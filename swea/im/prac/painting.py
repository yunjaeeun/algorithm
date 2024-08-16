'''
3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.

'''
dr = [-1, 1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]


def is_possible(n, m):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "#":
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == "#":
                        return "impossible"
                    elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == "?":
                        arr[nr][nc] = "."
                for k in range(4, 8):
                    nr, nc = i + dr[k], j + dc[k]
                    while 0 <= nr < n and 0 <= nc < m:
                        if arr[nr][nc] == ".":
                            return "impossible"
                        elif arr[nr][nc] == "?":
                            arr[nr][nc] == "#"
                        nr += dr[k]
                        nc += dc[k]
            elif arr[i][j] == ".":
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == ".":
                        return "impossible"
                    elif 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == "?":
                        arr[nr][nc] = "#"
                for k in range(4, 8):
                    nr, nc = i + dr[k], j + dc[k]
                    while 0 <= nr < n and 0 <= nc < m:
                        if arr[nr][nc] == "#":
                            return "impossible"
                        elif arr[nr][nc] == "?":
                            arr[nr][nc] == "."
                        nr += dr[k]
                        nc += dc[k]
    return "possible"


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    board = [[0] * M for _ in range(N)]

    result = is_possible(N, M)

    print(f"#{tc} {result}")
