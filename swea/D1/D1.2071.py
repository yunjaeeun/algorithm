t = int(input())

for i in range(t):
    num = 0
    arr = list(map(int, input().split(" ")))

    for j in range(len(arr)):
        num += arr[j]
    
    num = round(num/len(arr))
    print("#{0} {1}".format(i + 1, num))