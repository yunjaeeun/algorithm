'''
1
4 3
1 2 1 2

'''
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 수열의 길이, M : 합
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1 << N):
        subset_sum = 0
        for j in range(N):
            if i & (1 << j):
                subset_sum += arr[j]
            if subset_sum > M:
                break
        if subset_sum == M:
            result += 1

    print(f"#{tc} {result}")
