# 자릿수 더하기
a = input()
num = 0

for i in range(0, 4):
    for j in range(1, 10):
        if a[i] == str(j):
            num += j

print(num)