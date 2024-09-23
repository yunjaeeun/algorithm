'''
1
15 9
1 4 2 5 6 2 7 3 8 9 11 3 12 14 14 9 15 1

'''


def find_p(x):
    if parents[x] == x:
        return x
    else:
        return find_p(parents[x])


def union(x, y):
    root_x = find_p(x)
    root_y = find_p(y)

    if root_x < root_y:
        child = root_y
        parent = root_x
    elif root_x > root_y:
        child = root_x
        parent = root_y
    else:
        child = root_x
        parent = root_x

    for i in range(1, N + 1):
        if parents[i] == child:  # 부모가 자식인거 전부 바꾸기
            parents[i] = parent


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    for i in range(M):
        union(arr[i * 2], arr[i * 2 + 1])

    start = parents[1]
    result = [parents[1]]
    for i in range(1, N + 1):
        if parents[i] not in result:
            result.append(parents[i])

    print(parents)
    print(f"#{tc} {len(result)}")
