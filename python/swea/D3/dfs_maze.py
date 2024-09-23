T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def find_three(start_i, start_j, end_i, end_j, N):
    stack = []
    visited = [[0] * N for _ in range(N)]
    visited[start_i][start_j] = 1
    stack.append([start_i, start_j])
    current_i = start_i
    current_j = start_j
    while True:
        if current_i == end_i and current_j == end_j:
            return 1

        for d in range(4):
            next_i = current_i + di[d]
            next_j = current_j + dj[d]
            if 0 <= next_i < N and 0 <= next_j < N and visited[next_i][next_j] == 0 and maze[next_i][next_j] != 1:
                stack.append([current_i, current_j])
                visited[next_i][next_j] = 1
                current_i = next_i
                current_j = next_j
                break
        else:
            if stack:
                idx = stack.pop()
                current_i = idx[0]
                current_j = idx[1]
            else:
                return 0


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                end_i, end_j = i, j
            elif maze[i][j] == 2:
                start_i, start_j = i, j
                break
    result = find_three(start_i, start_j, end_i, end_j, N)

    print(f"#{tc} {result}")
