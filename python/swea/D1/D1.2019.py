t = int(input())
num = 1
for i in range(t + 1):
    if i == 0:
        print(1, end=" ")
    else:
        num *= 2
        print(num, end=" ")