'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.

'''

T = int(input())
    # 하 오른대각선, 왼대각선, 우
dr = [1, 1, 1, 0]
dc = [0, 1, -1, 1]


def find_gomoku(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                # 아래 탐색
                count = 1
                nr = i
                nc = j
                for _ in range(4):
                    nc += dc[3]
                    if nc < N:
                        if arr[nr][nc] == ".":
                            count = 1
                            break
                        else:
                            count += 1
                if count == 5:
                    return "YES"
                else:
                    nc = j
                    count = 1

                for _ in range(4):
                    nr += dr[0]
                    if nr < N:
                        if arr[nr][nc] == ".":
                            count = 1
                            break
                        else:
                            count += 1
                if count == 5:
                    return "YES"
                else:
                    nr = i
                    nc = j
                    count = 1

                # 오른 대각선 탐색
                for _ in range(4):
                    nr += dr[1]
                    nc += dc[1]
                    if nr < N and nc < N:
                        if arr[nr][nc] == ".":
                            count = 1
                            break
                        else:
                            count += 1
                if count == 5:
                    return "YES"
                else:
                    nr = i
                    nc = j
                    count = 1

                # 왼쪽 대각선 탐색
                for _ in range(4):
                    nr += dr[2]
                    nc += dc[2]
                    if nr < N and nc >= 0:
                        if arr[nr][nc] == ".":
                            count = 1
                            nr = i
                            nc = j
                            break
                        else:
                            count += 1
                if count == 5:
                    return "YES"
    return "NO"


for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    result = find_gomoku(N)

    print(f"#{tc} {result}")
