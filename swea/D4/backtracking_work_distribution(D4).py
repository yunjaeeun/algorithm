def find_max(per_sum, cnt, idx):
    global result

    if cnt == N:
        if per_sum > result:
            result = per_sum

    if per_sum <= result:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find_max(per_sum * arr[idx][i] * 0.01, cnt + 1, idx + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    result = 0
    find_max(1, 0, 0)
    result = result * 100

    print(f"#{tc} {result:.6f}")

'''
1
3
13 0 50
12 70 90
25 60 100

'''
