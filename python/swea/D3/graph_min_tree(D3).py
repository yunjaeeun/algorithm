'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''
from heapq import heappop, heappush


def prim(start):
    heap = []

    sum_weight = 0  # 총 비용
    heappush(heap, (0, start))  # 가중치, 도착지점

    while heap:
        weight, v = heappop(heap)   # 최소힙이기 때문에 가중치가 작은것이 pop됨

        if MST[v]:  # 방문한적 있다면 패스
            continue

        MST[v] = 1      # 방문 체크
        sum_weight += weight        # 총 비용 업데이트

        for next_v, next_w in graph[v]:     # 다음으로 갈 수 있는 노드 확인
            if MST[next_v]:     # 방문한적 있으면 패스(사이클 방지)
                continue

            heappush(heap, (next_w, next_v))    # 힙에 추가

    return sum_weight


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    # V = 노드의 수, E = 간선의 수
    graph = [[] for _ in range(V + 1)]  # 인접리스트로 저장
    MST = [0] * (V + 1)     # 방문을 체크할 배열(트리의 사이클을 막기 위해)
    for _ in range(E):
        s, e, c = map(int, input().split()) # 시작지점, 종료지점, 가중치
        graph[s].append((e, c)) # 무향이기 떄문에 둘 다 저장
        graph[e].append((s, c))

    result = prim(0)    # 시작 지점은 0으로 설정
    print(f"#{tc} {result}")
