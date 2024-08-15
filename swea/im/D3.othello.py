'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

'''
def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N


T = int(input())
# 상 하 좌 우 좌하 좌상 우하  좌상
dr = [-1, 1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]

    if N == 4:
        board[1][1] = 2
        board[2][1] = 1
        board[1][2] = 1
        board[2][2] = 2
    if N == 8:
        board[3][3] = 2
        board[3][4] = 1
        board[4][3] = 1
        board[4][4] = 2

    for _ in range(M):
        cr, cc, stone = map(int, input().split())
        cr -= 1
        cc -= 1
        board[cr][cc] = stone
        for i in range(8):
            nr, nc = cr + dr[i], cc + dc[i]
            lr = lc = -1
            while is_valid(nr, nc):
                if board[cr][cc] == board[nr][nc]:
                    lr, lc = nr, nc
                    break
                nr += dr[i]
                nc += dc[i]
            if lr != -1 and lc != -1:
                while cr != nr and cc != nc:
                    if board[nr][nc] != stone and board[nr][nc] != 0:
                        board[nr][nc] = stone
                    nr -= dr[i]
                    nc -= dc[i]

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f"#{tc} {black} {white}")