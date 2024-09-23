T = int(input())

for i in range(T):
    N = int(input())
    arr = []
    result = []
    for j in range(N):
        maze = list(map(int, input().split()))
        arr.append(maze)
    
    print(arr)