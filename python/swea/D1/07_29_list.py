'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

'''

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    start = M // 2

    result = []
    for i in range(start, N - start):
        dummy = arr[i - start: i + start + 1]

        num = 0
        for j in range(M):
            num += dummy[j]
        
        result.append(num)

    max_v = result[0]
    min_n = result[0]
    for value in result:
        if value < min_n:
            min_n = value
        if value > max_v:
            max_v = value
        
    print(f"#{tc} {max_v - min_n}")
