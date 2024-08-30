'''
3
11
128
2147483645

'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    result = 0
    while N != 0:
        if N % 2 == 1:
            result += 1
        N //= 2

    print(f"#{tc} {result}")

