t = int(input())

for i in range(t):
    arr = list(map(int, input().split(" ")))

    temp = 0
    for j in range(len(arr)):
        if temp < arr[j]:
            temp = arr[j]

    print("#{0} {1}".format(i + 1, temp))