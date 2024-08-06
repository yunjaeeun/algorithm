'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

'''
T = int(input())

for tc in range(1, T + 1):
    arr_1 = list(input())
    arr_2 = list(input())

    result = 0

    for str_1 in arr_1:
        count = 0
        for value in arr_2:
            if str_1 == value:
                count += 1

        if count > result:
            result = count

    print(f"#{tc} {result}")
