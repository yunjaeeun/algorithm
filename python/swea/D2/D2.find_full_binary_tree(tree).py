'''
2
7
1 2 2 3 4 4 3
15
1 2 2 3 3 3 3 4 7 4 7 4 7 4 7

'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = True
    cnt = 1
    last_idx = 1
    while cnt < N:
        mid = cnt
        cnt *= 2
        left = arr[last_idx:last_idx + mid]
        right = arr[last_idx + mid: last_idx + cnt]
        right = right[::-1]
        print(left)
        print(right)
        if left != right:
            result = False
            break
        last_idx += cnt

    print(f"#{tc} {result}")
