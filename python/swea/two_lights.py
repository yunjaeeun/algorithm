'''
3
1 3 5 7
0 5 2 4
0 5 1 6

'''
T = int(input())
lst = []
for tc in range(1, T + 1):
    x_s, x_e, y_s, y_e = map(int, input().split())
    start = max(x_s, y_s)
    end = min(y_e, x_e)
    result = end - start
    if result <= 0:
        result = 0

    lst.append(result)

for index, value in enumerate(lst):
    print(f"#{index + 1} {value}")
