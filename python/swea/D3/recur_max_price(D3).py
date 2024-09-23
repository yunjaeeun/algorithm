'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

'''

# T = int(input())
#
#
# def find_max(price, cnt, c_idx):
#     global result
#     if cnt == 0:
#         c_price = ""
#         for char in price:
#             c_price += char
#
#         if int(c_price) > result:
#             result = int(c_price)
#         return
#
#     for j in range(c_idx + 1, len(price)):
#         price[c_idx], price[j] = price[j], price[c_idx]
#         find_max(price, cnt -1, j)
#
#
# for tc in range(1, T + 1):
#     N, M = input().split()
#     M = int(M)
#     result = int(N)
#     N = list(N)
#
#     find_max(N, M, 0)
#
#     print(f"#{tc} {result}")

def find_max(price, cnt, c_idx, visited):
    global result

    # 교체 횟수를 모두 사용한 경우 최대값 갱신
    if cnt == 0:
        current_price = int("".join(price))
        if current_price > result:
            result = current_price
        return

    # 현재 상태와 남은 교체 횟수를 기준으로 방문 체크
    state = (tuple(price), cnt)
    if state in visited:
        return
    visited.add(state)

    # 가능한 모든 교체 시도
    for i in range(c_idx, len(price)):
        for j in range(i + 1, len(price)):
            # 스왑
            price[i], price[j] = price[j], price[i]
            find_max(price, cnt - 1, i, visited)
            # 원상복구
            price[i], price[j] = price[j], price[i]


T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    N = list(N)
    result = 0
    visited = set()

    find_max(N, M, 0, visited)

    print(f"#{tc} {result}")
