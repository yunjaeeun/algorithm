'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

'''
T = int(input())


def find_min(r, c, ctn):
    global result
    if ctn > result:
        return

    if r == N or c == N:
        return

    if r == N - 1 and c == N - 1:
        ctn += arr[r][c]
        if ctn < result:
            result = ctn
        return

    ctn += arr[r][c]
    find_min(r + 1, c, ctn)
    find_min(r, c + 1, ctn)


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 100000

    find_min(0, 0, 0)

    print(f"#{tc} {result}")
