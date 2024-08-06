# 중간값 찾기
n = int(input())

arr = list(map(int, input().split(" ")))

arr.sort()

print(arr[int(n/2)])
