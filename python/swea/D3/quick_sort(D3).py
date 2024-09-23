def partition(l, r):
    pivot = arr[l]
    i = l + 1
    j = r

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(l, r):
    if l < r:
        pivot = partition(l, r)
        quick_sort(l, pivot - 1)
        quick_sort(pivot + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print(f"#{tc} {arr[N//2]}")
