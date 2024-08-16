'''
3
5 1
5 2
100 3

'''
T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())

    result = N//(D * 2 + 1)

    if  N / (D * 2 + 1) - N//(D * 2 + 1) != 0:
        result += 1
    # garden = [0] * N
    #
    # result = 0
    # for i in range(D, N, D * 2 + 1):
    #     result += 1
    #     garden[i] = 1
    #     for j in range(1, D + 1):
    #         garden[i + j] = 1
    #         garden[i - j] = 1

    # print(garden)

    print(f"#{tc} {result}")
