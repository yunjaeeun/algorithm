'''
3
||||||
(|..|)
.|.(|...||)|...()..

'''
T = int(input())

for tc in range(1, T + 1):
    grass = input()
    result = 0
    stack = []

    for i in range(len(grass)):
        next_idx = 1
        if grass[i] == "(":
            while i + next_idx < len(grass):
                if grass[i + next_idx] == "|" or grass[i + next_idx] == ")":
                    result += 1
                    break
                next_idx += 1
        if grass[i] == ")":
            while i - next_idx >= 0:
                if grass[i - next_idx] == "(":
                    break
                elif grass[i - next_idx] == "|":
                    result += 1
                    break
                next_idx += 1

    print(f"#{tc} {result}")
