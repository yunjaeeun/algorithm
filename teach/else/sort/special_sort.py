'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

'''


def special_sort(arr, special_arr):
    max_n = arr[0]
    min_n = arr[0]
    max_idx = 0
    min_idx = 0
    for idx in range(len(arr)):
        if arr[idx] < min_n:
            min_n = arr[idx]
            min_idx = idx
        elif arr[idx] > max_n:
            max_n = arr[idx]
            max_idx = idx
    special_arr.append(arr[max_idx])
    special_arr.append(arr[min_idx])

    arr.remove(max_n)
    arr.remove(min_n)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    special_arr = []

    for i in range(5):
        special_sort(arr, special_arr)

    print(f"#{tc}", end=" ")
    for i in range(10):
        if i == 9:
            print(special_arr[i])
        else:
            print(special_arr[i], end=" ")
