'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2

'''
# 접근방법
# 1. 전체 배열을 순회하면서 확인한다.
# 2. 인접한 방의 숫자가 현재 방보다 1 크면 visited 1 체크

T = int(input())
# direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)     # 숫자가 겹치지 않으니까

    # 전체를 순회하며
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]

                # 범위 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                # 내 옆이 나보다 1 크다면, 나는 다음으로 갈 수 있는 방이다.
                if arr[ny][nx] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    # 이미 체크된 순간, 다른 방향을 볼 필요가 없음
                    # 이유: 동일한 숫자가 없기 때문에
                    break

    cnt = max_cnt = start = 0

    for i in range(N * N - 1, -1, -1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0

    print(f"#{tc} {start} {max_cnt + 1}")
