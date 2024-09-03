# 단계
# now : 현재 내가 방문한 구역 번호
# v : 지금까지 순열을 만드는데 사용했던 인덱스 번호(중복체크)
# e_sum : now 자리까지 정했을 때 에너지 사용량 합
def perm(now, e_sum, v):
    # 종료조건
    # 모든 방을 다 방문했으면 종료
    if len(v) == N:
        return
    # 재귀호출
    # 다음에 갈 수 있는 구역의 번호를 탐색
    # 0부터 N - 1까지
    # 갈 수 있는 구역의 번호? 내가 이전에 간적이 없는 번호면 갈 수 있다.
    for next in range(N):
        # next번 구역을 이번 차례에 갔다고 처리하고 다음 차례 방을 고르러 출벌
        if next not in v:
            perm(next, e_sum + energy[now][next], v + [next])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 구역의 개수
    energy = [list(map(int, input().split())) for _ in range(N)]
    # 각 구역으로 이동할 때 마다 사용하는 배터리 양
    # energy[i][j] => 1버 방에서 j번 방으로 이동하는데 사용하는 배터리 양
    # energy[i][j] != energy[j][i]
