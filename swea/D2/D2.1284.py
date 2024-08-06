T = int(input())

for i in range(T):
    arr = list(map(int, input().split(" ")))

    if arr[2] > arr[-1]:
        if arr[0] * arr[-1] > arr[1]:
            print(arr[1])
        else:
            print(f"#{i + 1}" + (arr[0] * arr[-1]))
    else:
        if arr[0] * arr[-1] > arr[1] + (arr[-1] - arr[2]) * arr[-2]:
            print(f"#{i + 1}" + (arr[1] + (arr[-1] - arr[2]) * arr[-2]))
        else:
            print(f"#{i + 1}" + (arr[0] * arr[-1]))