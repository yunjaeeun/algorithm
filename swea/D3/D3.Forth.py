'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

'''


def calculate(arr):
    stack = []
    not_num = ["-", "+", "*", "/", "."]

    for value in arr:
        if value not in not_num:
            stack.append(int(value))
        else:
            if value == ".":
                if len(stack) == 1:
                    return stack.pop()
                else:
                    return "error"

            elif len(stack) < 2:
                return "error"

            else:
                right = stack.pop()
                left = stack.pop()
                if value == "-":
                    num = left - right
                    stack.append(num)
                elif value == "+":
                    num = left + right
                    stack.append(num)
                elif value == "*":
                    num = left * right
                    stack.append(num)
                elif value == "/":
                    if right == 0 or left == 0:
                        return "error"
                    num = left / right
                    stack.append(int(num))
    return "error"


T = int(input())

for tc in range(1, T + 1):
    arr = list(input().split())

    cal = calculate(arr)

    print(f"#{tc} {cal}")
