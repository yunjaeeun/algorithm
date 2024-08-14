'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

'''


def bfs(s, e):
    visited = [0] * (V + 1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)

        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

        if t == e:
            return visited[t] - 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_l = [[] for _ in range(V + 1)]

    for i in range(E):
        start, end = map(int, input().split())
        adj_l[start].append(end)
        adj_l[end].append(start)

    S, G = map(int, input().split())

    result = bfs(S, G)

    print(f"#{tc} {result}")
