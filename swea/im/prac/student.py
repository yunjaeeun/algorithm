'''
3
2
0 1 0 0 0 0 0
100000
1 0 0 0 1 0 1
1
1 0 0 0 0 0 0

'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = []
    for i in range(7):
        ctn = N
        ci = i
        num = 0
        while ctn != 0:
            if ci == 7:
                ci = 0

            if arr[ci] == 1:
                ctn -= 1

            num += 1
            ci += 1
        result.append(num)

    print(f"#{tc} {min(result)}")