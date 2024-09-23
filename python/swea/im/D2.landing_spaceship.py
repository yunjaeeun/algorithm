'''
3
3 5
2 3 1 8 9
7 6 2 2 6
5 7 3 8 7
5 5
5 2 3 5 2
5 5 8 4 5
3 6 8 5 2
8 2 3 3 3
5 1 5 4 5
5 8
8 7 2 5 2 4 3 1
7 4 2 3 9 3 5 1
5 7 6 2 2 7 9 6
9 8 7 6 2 1 9 4
1 9 4 9 2 3 5 2
10 5
6 1 2 3 3
5 2 4 6 9
2 3 8 4 5
4 9 7 4 3
2 8 5 9 7
6 1 8 7 4
1 4 5 8 6
5 6 2 8 5
4 2 9 8 2
1 9 9 6 9

'''

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M


T = int(input())
# 상 하  좌 우 우하 우상 좌하 좌상
dr = [-1, 1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    landing_spot = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):      # 착륙위치 전체 탐색
        for j in range(M):
            current_height = landing_spot[i][j]     # 현재 높이
            photo_count = 0     # 사진 찍을 수 있는 위치 카운트

            for k in range(8):  # 주위 8범위 탐색
                nr = i + dr[k]
                nc = j + dc[k]
                if is_valid(nr, nc) and landing_spot[nr][nc] < current_height:  # 인덱스가 벗어나지 않고 현재 높이보다 작다면
                    photo_count += 1        # 카운트 + 1

            if photo_count >= 4:    # 찍을 수 있는 위치가 4개 이상이면
                result += 1         # 착륙후보 +1

    print(f"#{tc} {result}")
