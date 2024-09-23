T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]
    color_cnt = []

    result = 0
    isBlue = False
    isRed = False
    for i in range(N):
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        for j in range(M):
            # 최소조건
            if i == 0 and flag[i][j] != "W":
                result += 1
            elif i == N - 1 and flag[i][j] != "R":
                result += 1

            if flag[i][j] == "W":
                w_cnt += 1
            elif flag[i][j] == "R":
                r_cnt += 1
            else:
                b_cnt += 1
        if not isBlue:
            if w_cnt > r_cnt + b_cnt:
                result += r_cnt + b_cnt
            elif b_cnt > r_cnt + w_cnt:
                result += r_cnt + w_cnt
                isBlue = True
        elif isBlue and not isRed:
            if b_cnt > w_cnt + r_cnt:
                result += w_cnt + r_cnt
            elif r_cnt > b_cnt + w_cnt:
                result += b_cnt + w_cnt
                isRed = True
        elif isRed:
            result += w_cnt + b_cnt
        # color_cnt.append([w_cnt, b_cnt, r_cnt])

    # print(color_cnt)

    # if isBlue and not isRed:
    #     pass
    #
    # if isRed:
    #     pass

    print(f"#{tc} {result}")
