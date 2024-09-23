'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

'''
T = int(input())

for tc in range(1, T + 1):
    str1 = input()

    str_len = len(str1)

    my_stack = []

    result = 1
    for i in range(str_len):
        if str1[i] == "(" or str1[i] == "{":
            my_stack.append(str1[i])

        if str1[i] == ")" or str1[i] == "}":
            if len(my_stack) == 0:
                result = 0
                break
            elif my_stack[-1] == "{" and str1[i] == "}":
                my_stack.pop()
            elif my_stack[-1] == "(" and str1[i] == ")":
                my_stack.pop()
            else:
                result = 0
                break

    if len(my_stack) != 0:
        result = 0

    print(f"#{tc} {result}")
