'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

'''
def get_sum(r, n, current_sum):
    global min_sum

    # 가지치기 (현재까지의 합이 이미 최소 합을 초과하면 더 이상 탐색하지 않는다)
    if current_sum >= min_sum:
        return

    # 모든 행을 다 탐색한 경우
    if r == N and n == 0:
        if current_sum < min_sum:
            min_sum = current_sum
        return
    for c in range(N):

        isCan = True
        # 1. 방문한적 없는지
        # 2. 놓을 수 있는 위치인지
        for i in range(r):
            if visited[i][c] == 1:
                isCan = False
                break

        # 다 가능하다면 방문
        if isCan:
            visited[r][c] = 1           # 방문 등록
            current_sum += arr[r][c]    # 경우의 수의 합 더하기
            get_sum(r + 1, n - 1, current_sum)  # 다음행 방문
            visited[r][c] = 0           # 방문 해제
            # 합계에서 현재 위치의 값을 다시 빼주기(같은 열의 다른 경우의 수도 탐색하기 위함)
            current_sum -= arr[r][c]



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]       # 방문 등록용 배열

    min_sum = 100    # 3<= N <= 10, 자연수 < 10

    get_sum(0, N, 0)
    print(f"#{tc} {min_sum}")
