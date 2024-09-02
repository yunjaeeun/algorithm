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

def find_max(price, cnt, c_idx, max_result):
    if cnt == 0:
        c_price = "".join(price)
        return max(max_result, int(c_price))

    for j in range(c_idx + 1, len(price)):
        price[c_idx], price[j] = price[j], price[c_idx]
        max_result = find_max(price, cnt - 1, c_idx + 1, max_result)
        price[c_idx], price[j] = price[j], price[c_idx]

    return max_result


T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    price_list = list(N)

    # Call find_max and initialize result
    result = find_max(price_list, M, 0, int(N))

    print(f"#{tc} {result}")
