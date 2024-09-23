dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def make_num(r, c, cnt, num):
    if cnt == 7:
        made.add(num)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nc < 0 or nc >= 4 or nr < 0 or nr >= 4:
            continue

        make_num(nr, nc, cnt + 1, num + arr[nr][nc])

T = int(input())

for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    made = set()
    for i in range(4):
        for j in range(4):
            make_num(i, j, 1, arr[i][j])
    result = len(made)

    print(f"#{tc} {result}")