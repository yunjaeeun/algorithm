T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    max_price = arr[-1]

    for i in range(N - 1, -1, -1):
        if arr[i] >= max_price:
            max_price = arr[i]
        result += max_price - arr[i]    # 가격이 같으면 어짜피 0, 뒤에서부터 순회하므로 어짜피 팔 수 있는 최댓값에 판다.

    print(f"#{tc} {result}")
