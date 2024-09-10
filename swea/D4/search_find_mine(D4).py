'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...

'''
dr = [1, -1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, 1, -1, -1, 1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def find_zero():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == ".":
                is_zero = True
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if is_valid(nr, nc):
                        if arr[nr][nc] != ".":
                            is_zero = False
                            break
                if is_zero:
                    zero_lst.append((r, c))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    zero_lst = []
    find_zero()
    print(zero_lst)