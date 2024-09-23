T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0

    for i in range(N):
        result = result ^ arr[i]    # 특정 수로 2회 XOR를 하면 원래 수로 돌아옴
    print(f"#{tc} {result}")
