import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    find_idx = 0

    for i in range(100):
        if ladder[99][i] == 2:
            find_idx = i
    current_i = 99
    current_j = find_idx

    while current_i > 0:
        if current_j + 1 < 100 and ladder[current_i][current_j + 1] == 1:
            while current_j + 1 < 100 and ladder[current_i][current_j + 1] == 1:
                current_j += 1
        elif current_j - 1 >= 0 and ladder[current_i][current_j - 1] == 1:
            while current_j - 1 >= 0 and ladder[current_i][current_j - 1] == 1:
                current_j -= 1
        current_i -= 1

    print(f"#{tc} {current_j}")
