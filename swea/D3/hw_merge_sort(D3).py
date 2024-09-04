def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]


    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)

    print(f"#{tc} {arr[N//2]} {cnt}")

'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

'''