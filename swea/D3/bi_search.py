def binary_search(total_page, find_page):
    start = 1
    end = total_page
    count = 0
    while start <= end:
        count += 1
        mid = int((start + end)/2)

        if mid < find_page:
            start = mid
        elif mid > find_page:
            end = mid
        else:
            return count

T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    count_a = binary_search(P, A)
    count_b = binary_search(P, B)

    winner = ''
    if count_a < count_b:
        winner = "A"
    elif count_a > count_b:
        winner = "B"
    else:
        winner = 0

    print(f"#{tc} {winner}")
