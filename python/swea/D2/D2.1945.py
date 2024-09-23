T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * 5

    while True:
        if N == 1:
            break

        if N % 2 == 0:
            arr[0] += 1
            N /= 2

        if N % 3 == 0:
            arr[1] += 1
            N /= 3

        if N % 5 == 0:
            arr[2] += 1
            N /= 5

        if N % 7 == 0:
            arr[3] += 1
            N /= 7

        if N % 11 == 0:
            arr[4] += 1
            N /= 11

    print(f"#{tc}",end=" ")
    for i in range(5):
        if i == 4:
            print(arr[i])
        else:
            print(arr[i], end=" ")