T = int(input())

for i in range(T):
    input()
    arr = list(map(abs, map(int, input().split())))

    min_range = min(arr)

    min_count = 0

    for value in arr:
        if value == min_range:
            min_count += 1
    
    print(f"#{i + 1} {min_range} {min_count}")

