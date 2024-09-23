T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N //= 10
    print(N)

    arr = [0] * (N + 1)
    print(arr)
    arr[1] = 1
    arr[2] = 3

    for i in range(3, N + 1):
        # 왜 2(n-2) + 1??
        # 이 전 세트에 왼쪽, 오른쪽 한번씩 붙이기 -> 2(n-2) +
        # (n-1) -> 그냥 붙이기(그냥 붙여도 대칭)
        arr[i] = (arr[i - 2] * 2) + arr[i - 1]
        print(arr)

    print(f"#{tc} {arr[N]}")
