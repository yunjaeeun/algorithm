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
2 5
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


def dfs_l(s, e, V):
    visited = [0] * (V + 1)     # 방문한곳 1 방문x 0
    stack = []                  # 이태까지 왔던 경로
    visited[s] = 1              # 시작위치 방문 체크
    v = s                       # v = 현위치

    while True:
        if v == e:              # 종료지점에 도달하면
            return 1
        for i in adj_l[v]:      # 현 위치에서 갈 수 있는 경우의수 탐색 ex [[] ,[2], [1, 5]] v = 2일때 갈수있는 경우의 수 1 또는 5
            if visited[i] == 0: # 찾은 경우의 수를 방문하지 않았다면
                stack.append(v) # 왔던 경로에 추가
                visited[i] = 1  # 방문체크
                v = i           # 이동
                break
        else:                   # for else는 break가 실행되지 않으면 else문 실행
            if stack:           # 왔던 경로가 있으면
                v = stack.pop() # 되돌아가기
            else:
                return 0        # 왔던 경로가 없으면 0 리턴


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())        # V = 정점의 수, E = 간선의 수
    adj_l = [[] for _ in range(V + 1)]      # 현 위치에서 갈 수 있는 경우의 수를 인덱스에 맞게 담기 위함

    for i in range(E):
        s, e = map(int, input().split())  # s = 출발, e = 도착
        adj_l[s].append(e)                # 단방향이기 때문에 한번만 추가

    w_s, w_e = map(int, input().split())    # w_s 출발지점, w_e 종료지점

    result = dfs_l(w_s, w_e, V)

    print(f"#{tc} {result}")
