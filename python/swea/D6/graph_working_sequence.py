T = 10

# node : 현재 노드 번호
# visited : 중복 방문 체크
# stack : 스택
def dfs(node, visited, stack):
    visited.add(node)

    # node와 인접한 이웃 정점들 모두 탐색
    for next in G[node]:
        # 이전에 방문한적 없는 노드만
        if next not in visited:
            dfs(next, visited, stack)

    # node에서 갈 수 있는 모든 경로 탐색 완료
    stack.append(node)


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    G = [[] for _ in range(V + 1)]
    for i in range(E):
        s = edges[i * 2]
        e = edges[i * 2 + 1]
        # E번 작업을 하기 위해서는 S를 먼저 해야한다.
        # 작업순서 : S => E
        G[s].append(e)

    visited = set()
    stack = []
    # 모든 노드에서 dfs 탐색 시작 해보기
    # 단, 이전 탐색에서 방문한 적이 없는 노드만
    for v in range(1, V + 1):
        if v not in visited:
            dfs(v, visited, stack)

    print(f"#{tc}", *stack[::-1])