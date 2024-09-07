T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result_0, result_1 = 1, 0
    for i in range(N):
        result_0, result_1 = result_1, result_1 + result_0

    print(f"{result_0} {result_1}")
