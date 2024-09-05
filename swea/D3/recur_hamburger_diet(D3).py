def find_score(score, kcal, idx):
    global result
    if kcal > L:
        return

    if score > result:
        result = score

    remain_score = 0
    for i in range(N):
        if used[i] == 0:
            remain_score += arr[i][0]

    if remain_score + score <= result:
        return

    for i in range(idx, N):
        if used[i] == 0:
            used[i] = 1
            find_score(score + arr[i][0], kcal + arr[i][1], i + 1)
            used[i] = 0



T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [[0, 0] for _ in range(N)]
    used = [0] * N
    for i in range(N):
        s, k = map(int, input().split())
        arr[i][0] = s
        arr[i][1] = k

    result = 0
    find_score(0, 0, 0)

    print(f"#{tc} {result}")

'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400

'''
