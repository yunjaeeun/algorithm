X = int(input())

result = 0
sticks = [64, 32, 16, 8, 4, 2, 1]
for stick in sticks:
    if X >= stick:
        result += 1
        X -= stick
    if X == 0:
        break

print(result)