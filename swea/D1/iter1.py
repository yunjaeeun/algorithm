T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input()))

    count = 0
    max_count = 0
    for i in range(N):
        if arr[i] == 0:
            if count > max_count:
                max_count = count
                count = 0
        else:
            count += 1
    
    print(f"#{tc} {max_count}")