'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

'''

def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j


def find_root(n):
    start_r, start_c = find_start(n)

    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1

    while q:
        current_r, currnet_c = q.pop(0)
        if maze[current_r][currnet_c] == 3:
            return visited[current_r][currnet_c] - 2

        for d in range(4):
            nr = current_r + dr[d]
            nc = currnet_c + dc[d]

            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[current_r][currnet_c] + 1

    return 0


T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    result = find_root(N)
    print(f"#{tc} {result}")
