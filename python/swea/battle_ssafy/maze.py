dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def is_valid(r, c):
    return 0 <= r < 16 and 0 <= c < 16

def find_root(r, c):
    if r == end[0] and c == end[1]:
        return 1  # 경로를 찾았을 경우 1 반환
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if is_valid(nr, nc) and arr[nr][nc] != "1" and visited[nr][nc] != 1:
            visited[nr][nc] = 1
            if find_root(nr, nc):  # 재귀 호출 결과를 체크
                return 1  # 경로를 찾으면 1 반환
    return 0  # 경로가 없을 경우 0 반환

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    start = [0, 0]
    end = [0, 0]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == "2":
                start[0] = i
                start[1] = j
                visited[i][j] = 1
            elif arr[i][j] == "3":
                end[0] = i
                end[1] = j

    result = find_root(start[0], start[1])

    print(f"#{tc} {result}")
