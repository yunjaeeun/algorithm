T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    num = N
    arr = []
    while True:
        for char in str(num):
            if char not in arr:
                arr.append(char)
        if len(arr) == 10:
            result = num
            break

        num += N
    print(f"#{tc} {result}")