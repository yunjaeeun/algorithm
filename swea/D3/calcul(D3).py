'''
3
2 7
3 15
36 1007

'''
from collections import deque


def find_min(n, m):
    deq = deque()
    deq.append((n, 0))  # (숫자, 연산횟수)
    used[n] = 1

    while deq:  # BFS
        num, cnt = deq.popleft()

        if num == m:  # 너비우선 탐색이기 때문에 최소횟수 보장
            return cnt

        for nxt in (num + 1, num - 1, num * 2, num - 10):
            if not used[nxt] and num <= 1000000:
                deq.append((nxt, cnt + 1))  # 연산한 숫자, 연산횟수 덱에 추가
                used[nxt] = 1  # 연산 완료한 숫자 등록


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    used = [0] * 10000001
    result = find_min(N, M)
    print(f"#{tc} {result}")
