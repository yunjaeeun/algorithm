def dfs():
    v = 0                   # 시작위치
    visited = [0] * 100     # 방문 기록 배열
    stack = []              # 경로 저장

    while True:
        if v == 99:         # 성공적으로 도착하면 1 리턴
            return 1

        for i in adj_l[v]:
            if visited[i] == 0: # 방문하지 않았다면
                stack.append(i) # 지나온 경로 등록
                visited[i] = 1  # 방문 등록
                v = i   # 위치 이동
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return 0


for _ in range(10):
    tc, E = map(int, input().split())  # tc = 테스트케이스 번호, E = 경로 갯수

    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(99)]  # 경로를 기록할 배열
    for i in range(E):
        s = arr[i * 2]
        e = arr[i * 2 + 1]
        adj_l[s].append(e)

    result = dfs()

    print(f"#{tc} {result}")
