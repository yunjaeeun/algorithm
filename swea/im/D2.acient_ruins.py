'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1

'''


def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M


T = int(input())
# 우, 하 -> 시작점부터 오른쪽, 아래만 체크해도 최대범위를 알 수 있음
dr = [1, 0]
dc = [0, 1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    photo = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            if photo[i][j] == 1:    # 1을 찾으면 현재 위치부터 아래길이, 오른쪽길이 체크
                for k in range(2):
                    current_len = 1
                    nr = i + dr[k]
                    nc = j + dc[k]

                    while is_valid(nr, nc) and photo[nr][nc] == 1:
                        current_len += 1
                        nr += dr[k]
                        nc += dc[k]

                    if current_len > result:
                        result = current_len

    print(f"#{tc} {result}")
