T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    current_i = 0
    current_j = 0
    current_move = 'right'
    for i in range(1, N * N + 1):
        snail[current_i][current_j] = i
        if current_move == 'right' and current_j + 1 < N and snail[current_i][current_j + 1] == 0:
            current_j += 1
            if current_j + 1 >= N or snail[current_i][current_j + 1] != 0:
                current_move = 'down'
        elif current_move == 'down' and current_i + 1 < N and snail[current_i + 1][current_j] == 0:
            current_i += 1
            if current_i + 1 >= N or snail[current_i + 1][current_j] != 0:
                current_move = 'left'
        elif current_move == 'left' and current_j - 1 >= 0 and snail[current_i][current_j - 1] == 0:
            current_j -= 1
            if current_j - 1 < 0 or snail[current_i][current_j - 1] != 0:
                current_move = 'up'
        elif current_move == 'up' and current_i - 1 >= 0 and snail[current_i - 1][current_j] == 0:
            current_i -= 1
            if current_i - 1 < 0 or snail[current_i - 1][current_j] != 0:
                current_move = 'right'
    print(f"#{tc}")
    for i in range(N):
        print(*snail[i])
