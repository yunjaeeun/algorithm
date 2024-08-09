def change_postfix(formula, N):
    stack = []
    post = ""
    for i in range(N):
        if formula[i] != "+":
            post += formula[i]
        else:
            while stack:
                post += stack.pop()

            stack.append(formula[i])

    while stack:
        post += stack.pop()
    return post


def cal_postfix(postfix):
    stack = []
    for i in range(len(postfix)):
        if postfix[i] != "+":
            stack.append(int(postfix[i]))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    formula = input()

    postfix = change_postfix(formula, N)

    result = cal_postfix(postfix)

    print(f"#{tc} {result}")
