def find_min(r, cnt):
    global result
    if cnt >= result:
        return

    if r == N:
        if cnt < result:
            result = cnt
        return

    for i in range(N):
        if visited[i] == 1:
           continue

        visited[i] = 1
        find_min(r + 1, cnt + arr[r][i])
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 2000000
    find_min(0, 0)

    print(f"#{tc} {result}")

'''
3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4

'''
