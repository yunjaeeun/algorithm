'''
4
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
8
1 2 1 2 3 1 2 1

'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 1
    result = 1
    for i in range(1, N):
        if arr[i - 1] < arr[i]:
            count += 1        
        else:
            count = 1
        
        if count > result:
            result = count
        
    
    print(f"#{tc} {result}")