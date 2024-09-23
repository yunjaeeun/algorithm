operator = {"+": 1, "-": 1, "*": 2, "/": 2}


def change_post(N, formula):
    post = ""  # 리턴할 후위연산식
    stack = []  # 순서를 맞출 스택

    for i in range(N):
        if formula[i] not in "+-/*":  # 연산자가 아니면
            post += formula[i]  # 후위 연산식에 추가
        else:
            # 스택이 비어있지 않고, 스택 안에 있는 연산자의 우선순위가 더 높으면 추가
            while stack and operator[formula[i]] <= operator[stack[-1]]:
                post += stack.pop()
            # 스택이 비어있거나 연산자의 우선순위가 더 낮으면 추가
            stack.append(formula[i])
    while stack:  # 스택에 연산자가 남았을 경우를 생각하여 순서대로 연산자에 추가
        post += stack.pop()

    return post


def calculate_post(post_infix, N):
    statk = []
    for i in range(N):
        if post_infix[i] not in "-+*/":  # 숫자면 스택에 추가
            statk.append(int(post_infix[i]))
        else:  # 연산자가 나오면 계산 후 결과값을 다시 스택에 추가
            right = statk.pop()
            left = statk.pop()
            if post_infix[i] == "-":
                num = left - right
                statk.append(num)
            elif post_infix[i] == "+":
                num = left + right
                statk.append(num)
            elif post_infix[i] == "*":
                num = left * right
                statk.append(num)
            elif post_infix[i] == "/":
                num = left / right
                statk.append(num)

    return statk.pop()


for tc in range(1, 11):
    N = int(input())  # 계산식의 길이
    formula = input()  # 계산식

    post_infix = change_post(N, formula)

    result = calculate_post(post_infix, N)
    print(f"#{tc} {result}")
