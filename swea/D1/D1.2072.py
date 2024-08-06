t = int(input())

for i in range(t):
    num = 0
    arr = list(map(int, input().split(" ")))
    
    for j in range(len(arr)):
        if arr[j]%2 != 0:
            num += arr[j]
    
    print("#{0} {1}".format(i + 1, num))