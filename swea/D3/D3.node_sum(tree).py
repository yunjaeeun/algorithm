'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

'''


def make_tree(t):
    if t <= N:
        make_tree(t * 2)
        make_tree(t * 2 + 1)
        if t * 2 + 1 <= N:
            arr[t] = arr[t * 2] + arr[t * 2 + 1]
        elif t * 2 + 1 > N and t * 2 <= N:
            arr[t] = arr[t * 2]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # N: 노드의 개수, M: 리프 노드의 개수, L: 출력할 노드 번호
    arr = [0] * (N + 1)

    for _ in range(M):
        node_num, node_value = map(int, input().split())
        arr[node_num] = node_value

    make_tree(1)

    # print(arr)

    print(f"#{tc} {arr[L]}")
