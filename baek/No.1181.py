N = int(input())
arr = set()
for i in range(N):
    arr.add(input())
arr = list(arr)
arr.sort()
arr.sort(key=len)

for s in arr:
    print(s)



