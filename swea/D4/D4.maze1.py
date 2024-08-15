'''
1
1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111
2
1111111111111111
1200000010000011
1011111011111011
1000001010000011
1110101010111011
1010101010100011
1011111010111111
1000001010000011
1011101011111011
1010101010000011
1010101010111111
1010100000130011
1010111111111011
1000000000000011
1111111111111111
1111111111111111
3
1111111111111111
1210001000100011
1010101010101011
1000100010101011
1011111110101011
1000001010101011
1111101010101011
1010001000001011
1010111111111011
1010000000100011
1011111110101111
1000001010100011
1011101010111011
1000100000130011
1111111111111111
1111111111111111
4
1111111111111111
1200100000000011
1011101110111011
1000001010101011
1111111011101011
1000100010000011
1010101010111111
1010001010001011
1011111011101011
1000100010100011
1110101110111111
1010100000130011
1010111111111011
1000000000000011
1111111111111111
1111111111111111
5
1111111111111111
1210000000100011
1010111011101011
1010100010001011
1011101010111011
1000001010001011
1111111011111011
1000100010000011
1011101010111011
1010001000001011
1010101011111111
1010101000000011
1010101110111011
1000100010001311
1111111111111111
1111111111111111
6
1111111111111111
1210001010000011
1010101010111111
1010100000100011
1010111111101011
1000100000001011
1110101111111011
1000100000001011
1011101111101011
1000101000101011
1110101010111011
1010100010100011
1010111110101111
1000000000100311
1111111111111111
1111111111111111
7
1111111111111111
1210000000000011
1011101111111011
1000101010000011
1110101010111011
1000001000101011
1010111111101111
1010100000100011
1011101110101111
1000001000100011
1111111011111011
1000100010001011
1010101110111011
1010001300000011
1111111111111111
1111111111111111
8
1111111111111111
1200000010000011
1111111010111011
1000000010001011
1011111111111011
1010000000000011
1010111111101011
1010000000001011
1010111011111011
1000100010001011
1111111011101011
1000001000100011
1110111110101011
1000000000101311
1111111111111111
1111111111111111
9
1111111111111111
1200000000001011
1011111111101011
1000000010001011
1111111010111011
1000100010000011
1011101111111011
1010001000001011
1010111011101011
1010000010101311
1011111110101111
1000100000100011
1011101011111011
1000001000000011
1111111111111111
1111111111111111
10
1111111111111111
1200001000100011
1111101110101011
1000100010001011
1011101111101111
1000100000000011
1110111111101011
1000000010001011
1110111011101011
1010001000001011
1010101111111011
1000101010000011
1010101010101111
1010100000100311
1111111111111111
1111111111111111

'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_root(sr, sc):
    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        cr, cc = q.pop()

        if maze[cr][cc] == 3:
            return 1

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 0


def find_start_idx():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    sr, sc = find_start_idx()

    result = find_root(sr, sc)
    print(f"#{tc} {result}")