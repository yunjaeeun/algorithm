N = int(input())

result = 0
while N != 0:
    if N - 5 < 0 and N - 3 < 0:
        result = -1
        break

    if N % 5 == 0 or N % 5 == 3:
        N -= 5
        result += 1
        continue
    else:
        N -= 3
        result += 1
print(result)
