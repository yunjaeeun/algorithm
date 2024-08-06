num = int(input())

arr = ["3", "6", "9"]

for i in range(1, num + 1):
    rep = 0
    for j in range(len(str(i))):
        if str(i)[j] in arr:
            rep += 1
    if rep != 0:
        print("-" * rep, end=" ")
    else:
        print(i, end=" ")