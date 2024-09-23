# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#
#     result = 0
#     while not (arr[0] < arr[1] < arr[2]):
#
#         if 0 == arr[1] or 0 == arr[2]:
#             result = -1
#             break
#         if arr[0] >= arr[1]:
#             arr[0] -= 1
#             result += 1
#         elif arr[1] >= arr[2]:
#             arr[1] -= 1
#             result += 1
#
#     print(f"#{tc} {result}")

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = 0

    while not (arr[2] > arr[1] > arr[0]):
        if arr[0] >= arr[1]:
            arr[0] -= 1
            result += 1
        if arr[1] >= arr[2]:
            arr[1] -= 1
            result += 1

        if 0 in arr:
            result = -1
            break
    print(f"#{tc} {result}")
