dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def find_max(ctn, r, c):
    global result
    global room_num

    if not is_valid(r, c):
        return

    if ctn >= result and room_num > arr[r][c]:
        result = ctn
        room_num = arr[r][c]

    for i in range(4):
        if visited[r][c] == 0:
            if is_valid(r + dr[i], c + dc[i]) and arr[r][c] + 1 == arr[r + dr[i]][c + dc[i]]:
                visited[r][c] = 1
                find_max(ctn + 1, r + dr[i], c + dc[i])
                visited[r][c] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    result = 0
    room_num = 10000

    find_max(0, 0, 0)

    print(f"#{tc} {result}")
