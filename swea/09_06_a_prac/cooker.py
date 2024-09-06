def make_subset(n):
    global result
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j)

        if len(subset) == 4:
            # print(subset)
            num_1 = arr[subset[0]][subset[1]] + arr[subset[1]][subset[0]]
            num_2 = arr[subset[2]][subset[3]] + arr[subset[3]][subset[2]]
            num_3 = arr[subset[1]][subset[2]] + arr[subset[2]][subset[1]]
            num_4 = arr[subset[0]][subset[3]] + arr[subset[3]][subset[0]]
            if abs(num_2 - num_1) < result:
                result = abs(num_2 - num_1)
            if abs(num_3-num_4) < result:
                result = abs(num_3-num_4)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = list(range(N))
    result = 1000000
    make_subset(N)

    print(f"#{tc} {result}")
