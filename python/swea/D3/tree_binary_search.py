#
# def make_sub(start, end):
#     if start > end:
#         return
#
#     # if end % 2 != 0:
#     #     mid = (start + end) // 2 + 1
#     # else:
#     mid = (start + end) // 2
#
#     my_node.append(num_arr[mid])
#     print(my_node)
#     make_sub(start, mid - 1)  # 왼쪽 서브트리
#
#     # 재귀 호출로 왼쪽과 오른쪽 서브트리 생성
#     make_sub(mid + 1, end)  # 오른쪽 서브트리
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     num_arr = list(range(1, N + 1))
#
#     my_node = []
#
#     make_sub(0, N - 1)
#
#     root_value = num_arr[(N - 1) // 2]
#
#     print(f"#{tc} {root_value} {my_node}")

# def make_sub(left_tree, right_tree):
#     if len(left_tree) == 0 or len(right_tree) == 0:
#         return
#     # if len(left_tree) != 2 and len(right_tree) != 2:
#     left_mid = len(left_tree) // 2
#     right_mid = len(right_tree) // 2
#
#     my_node.append(left_tree[left_mid])
#     my_node.append(right_tree[right_mid])
#     print(my_node)
#     l_left = left_tree[:left_mid]
#     l_right = left_tree[left_mid + 1:]
#     make_sub(l_left, l_right)
#     r_left = right_tree[:right_mid]
#     r_right = right_tree[right_mid + 1:]
#     make_sub(r_left, r_right)
#     if len(left_tree) == 2:
#         my_node.append(left_tree[1])
#         my_node.append(left_tree[0])
#         return
#     elif len(right_tree) == 2:
#         my_node.append(right_tree[1])
#         my_node.append(right_tree[0])
#         return
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     num_arr = list(range(1, N + 1))
#     my_node = []
#     root_node = N // 2
#     left = num_arr[:root_node]
#     right = num_arr[root_node + 1:]
#     my_node.append(num_arr[root_node])
#
#     make_sub(left, right)
#     print(my_node)
#
#     print(f"#{tc} {num_arr[N//2]} {my_node[int(N/2) - 1]}")

# def make_node(arr):
#     if len(arr) == 1:
#         my_node.append(arr[0])
#         return
#
#     # 중간값 추가
#     mid = len(arr) // 2
#     my_node.append(num_arr[mid])
#
#     if len(arr) > 2:
#         left = arr[:mid]
#         make_node(left)
#         right = arr[mid + 1:]
#         make_node(right)
#
#     if len(arr) == 2:
#         left = arr[0]
#         right = arr[1]
#         my_node.append(right)
#         my_node.append(left)
#         return
#
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     num_arr = list(range(1, N + 1))
#     my_node = []
#     make_node(num_arr)
#
#     print(my_node)

def make_tree(t):
    global cnt
    if t <= N:
        make_tree(t * 2)
        tree[t] = cnt
        cnt += 1
        make_tree(t * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)

    cnt = 1

    make_tree(1)

    print(f"#{tc} {tree[1]} {tree[int(N / 2)]}")
