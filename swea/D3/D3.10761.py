'''
3
4 B 2 O 1 O 2 B 4
3 B 5 B 8 O 100
2 O 2 O 1

'''
T = int(input())

for tc in range(1, T + 1):
    arr = list(input().split())

    btn_count = int(arr[0])
    b_count = 0
    o_count = 0

    robo_o = [0] * 101
    robo_b = [0] * 101

    for i in range(1, len(arr) - 1):
        if arr[i] == "B":
            robo_b[int(arr[i + 1])] = 1
            b_count += 1
        if arr[i] == "O":
            robo_o[int(arr[i + 1])] = 1
            o_count += 1

    result = 0
    o_idx = 1
    o_press = False
    b_idx = 1
    b_press = True
    while btn_count > 0:
        result += 1
        if robo_o[o_idx] == 1 and robo_b[b_idx] == 1 and b_idx == o_idx:
            if b_count > o_count:
                if b_press:
                    btn_count -= 1
                    b_idx += 1
                    b_count -= 1
                    b_press = False
                else:
                    b_press = True
        else:
            if robo_o[o_idx] == 1:
                if o_press:
                    btn_count -= 1
                    o_idx += 1
                    o_press = False
                    o_count -= 1
                else:
                    o_press = True
            else:
                o_idx += 1

            if robo_b[b_idx] == 1:
                if b_press:
                    btn_count -= 1
                    b_idx += 1
                    b_press = False
                    b_count -= 1
                else:
                    b_press = True
            else:
                b_idx += 1

    print(result)
