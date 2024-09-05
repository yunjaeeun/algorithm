def find_max(per_sum, cnt, idx):
    global result

    if cnt == N:    # 일을 수행한 횟수가 일의 수와 같다면(종료조건)
        if per_sum > result:    # 최댓값 업데이트
            result = per_sum

    # 성공확률이 최댓값보다 작거나 같으면(가지치기)
    # 소수끼리 곱하기 때문에 더 커질 가능성이 없음
    if per_sum <= result:
        return

    for i in range(N):
        if visited[i] == 0:     # 방문한적이 없다면
            visited[i] = 1
            find_max(per_sum * arr[idx][i] * 0.01, cnt + 1, idx + 1)    # 재귀 호출
            visited[i] = 0  # 방문 초기화


T = int(input())
for tc in range(1, T + 1):
    N = int(input())   # N: 직원, 일의 수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 성공확률
    visited = [0] * N   # 일을 수행했는지 체크할 배열

    result = 0
    find_max(1, 0, 0)
    result = result * 100

    print(f"#{tc} {result:.6f}")    # 소숫점 6자리 출력(7번째에서 반올림)