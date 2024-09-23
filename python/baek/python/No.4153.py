while True:
    arr = list(map(int, input().split()))

    if 0 in arr:
        break

    max_n = max(arr)
    min_n = min(arr)
    mid_n = -1
    for num in arr:
        if num < max_n and num != min_n:
            mid_n = num
            break

    if mid_n == -1:
        mid_n = mid_n

    if max_n ** 2 == (mid_n ** 2) + (min_n ** 2):
        print("right")
    else:
        print("wrong")
