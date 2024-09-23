T = int(input())

for i in range(T):
    a = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    print(f"#{i + 1}",end=" ")
    
    for i in range(a):
        if i == a - 1:
            print(arr[i])
        else:
            print(arr[i], end=" ")
