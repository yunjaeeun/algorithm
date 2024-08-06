'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    background = [[0] * 10 for _ in range(10)]

    for i in range(N):
        for j in range(arr[i][0], arr[i][2] + 1):
            for k in range(arr[i][1], arr[i][3] + 1):
                if background[j][k] == 0:
                    if arr[i][4] == 1:
                        background[j][k] = 'r'
                    else:
                        background[j][k] = 'b'

                if arr[i][4] == 1 and background[j][k] == 'b':
                    background[j][k] = 'p'

                if arr[i][4] == 2 and background[j][k] == 'r':
                    background[j][k] = 'p'

    for i in range(10):
        for j in range(10):
            if background[i][j] == 'p':
                result += 1

    print(f"#{tc} {result}")
