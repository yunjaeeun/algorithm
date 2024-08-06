def find_line_max(arr):
    line_max = 0
    for i in range(100):
        current_line = 0
        for j in range(100):
            current_line += arr[i][j]

        if current_line > line_max:
            line_max = current_line

    return line_max


def find_row_max(arr):
    row_max = 0
    for i in range(100):
        current_row = 0
        for j in range(100):
            current_row += arr[j][i]

        if current_row > row_max:
            row_max = current_row

    return row_max


def find_diagonal_max(arr):
    left_diagonal = 0
    right_diagonal = 0
    for i in range(100):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][99 - i]

    return max(left_diagonal, right_diagonal)


for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    row_max = find_row_max(arr)
    line_max = find_line_max(arr)
    diagonal_max = find_diagonal_max(arr)

    result = max(row_max, line_max, diagonal_max)

    print(f"#{N} {result}")
