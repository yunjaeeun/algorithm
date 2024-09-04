T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    find_arr = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    result = 0
    for num in find_arr:
        start = 0
        end = M - 1
        found = False
        while start <= end and not found:

            mid = (start + end) // 2
            if num_list[mid] > num:
                end = mid - 1
            elif num_list[mid] < num:
                start = mid + 1
            else:
                result += 1
                found = True
                break

    print(f"#{tc} {result}")
