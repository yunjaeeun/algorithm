T = int(input())

# 원소 = 1 ~ 12
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N = 부분집합 원소의 수, K = 부분집합의 합
    arr = list(range(1, 6))  # 1 ~ 12 # [1, 2, 3, 4, 5]
    arr_len = 5
    result = 0
    for i in range(1 << arr_len):   # 1 ~ 2^n  비트로 따지면 n칸의 모든 비트가 들어올 때 까지(모든 경우의 수)
        subset = []
        for j in range(arr_len):
            if i & (1 << j):     # 자릿수가 켜져있으면 추가    (부분집합 생성)   1을 J번 민다
                subset.append(arr[j])
                print(f"i = {i} j = {j} 시프트 연산 = {1 << j} arr[j] = {arr[j]} ")
        if len(subset) == N and sum(subset) == K:   # 문제조건(필터링)
            result += 1

    print(f"#{tc} {result}")

print(1 << 0)