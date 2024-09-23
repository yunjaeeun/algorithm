N = int(input())
for _ in range(N):
    arr = list(input())
    stack = []
    result = "YES"
    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append(arr[i])
        else:
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    result = "NO"
                    break
            else:
                result = "NO"
                break
    if stack:
        result = "NO"
    print(result)
