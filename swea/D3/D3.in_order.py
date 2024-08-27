def in_order(t):
    if t:
        in_order(c_left[t])
        print(my_node[t], end="")
        in_order(c_right[t])


for tc in range(1, 11):
    N = int(input())
    my_node = [0] * (N + 1)
    c_left = [0] * (N + 1)
    c_right = [0] * (N + 1)

    for _ in range(N):
        node_input = list(input().split())

        my_node[int(node_input[0])] = node_input[1]

        if len(node_input) > 2:
            c_left[int(node_input[0])] = int(node_input[2])
        if len(node_input) > 3:
            c_right[int(node_input[0])] = int(node_input[3])

    print(f"#{tc}", end=" ")
    in_order(1)
    print()

