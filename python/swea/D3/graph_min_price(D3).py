'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1

'''
import heapq
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

INF = int(1e9)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())    # 가로세로 칸수
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N * N + 1)]  # 연결리스트로 저장
    distance = [INF] * (N * N + 1)  # 거리정보 저장

    # 전체 위치를 탐색하며 갈 수 있는 방향들의 정보와 가중치 저장
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                c_node = (r * N) + c + 1
                if 0 <= nr < N and 0 <= nc < N:
                    n_node = (nr * N) + nc + 1
                    if arr[r][c] < arr[nr][nc]: # 높이가 더 높다면 가중치 계산 후 저장
                        graph[c_node].append((n_node, arr[nr][nc] - arr[r][c] + 1))
                    else:
                        graph[c_node].append((n_node, 1))

    dijkstra(1)

    print(f"#{tc} {distance[N * N]}")
