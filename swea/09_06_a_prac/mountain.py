def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def find_len(r, c, m_len, cnt):
    if not is_valid(r, c):
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if is_valid(nr, nc):
            if arr[nr][nc] < arr[r][c]:
                find_len(nr, nc, m_len + 1, cnt)
            elif arr[nr][nc] - arr[r][c] - 1 < cnt:
                diff_num = arr[nr][nc] - arr[r][c] - 1
                cnt -= diff_num
                arr[nr][nc] -= diff_num
                find_len(nr, nc, m_len + 1, cnt)
                arr[nr][nc] += diff_num
                cnt += diff_num
            else:
                return


T = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    high_idx = []
    max_height = 0
    for li in arr:
        if max_height < max(li):
            max_height = max(li)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                high_idx.append([i, j])

    for height in high_idx:
        find_len(height[0], height[1], 0, K)

    print(f"#{tc} {result}")
