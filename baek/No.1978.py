N = int(input())

arr = list(map(int, input().split()))

result = 0
for value in arr:
    is_true = True
    for i in range(2, value):
        if value % i == 0:
            is_true = False
            break
    if is_true and value > 1:
        result += 1

print(result)