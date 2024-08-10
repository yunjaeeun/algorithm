'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

'''

def find_winner(start, end):
    winner = arr[start]
    winner_idx = start

    for i in range(start, end - 1):
        if winner == 1:
            if arr[i + 1] == 2:
                winner = 2
                winner_idx = i + 1
            else:
                continue

        elif winner == 2:
            if arr[i + 1] == 3:
                winner = 3
                winner_idx = i + 1
            else:
                continue
        elif winner == 3:
            if arr[i + 1] == 1:
                winner = 1
                winner_idx = i + 1
            else:
                continue

    return winner, winner_idx


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    center = N // 2

    l_winner, l_idx = find_winner(0, center)
    r_winner, r_idx = find_winner(center, N)

    if l_winner == 1:
        if r_winner == 2:
            result = r_idx
        else:
            result = l_idx
    if l_winner == 2:
        if r_winner == 3:
            result = r_idx
        else:
            result = l_idx
    if l_winner == 3:
        if r_winner == 1:
            result = r_idx
        else:
            result = l_idx

    result += 1

    print(f"#{tc} {result}")