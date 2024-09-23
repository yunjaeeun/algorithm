'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

'''


def find_min(start, ctn):
    global min_num
    if min_num < ctn:
        return
    if start >= arr[0]:
        if ctn < min_num:
            min_num = ctn
        return

    # capacity = arr[start]
    for i in range(arr[start], 0, -1):
        find_min(start + i, ctn + 1)


    # while capacity > 0:
    #     find_min(start + capacity, ctn + 1)
    #     capacity -= 1


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    min_num = 100
    find_min(1, 0)
    print(f"#{tc} {min_num - 1}")
