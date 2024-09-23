def cal(t):
    if t:
        # 계산을 하기 위해서는 자식노드가 2개인지 확인 해야하므로 후위순회
        cal(left[t])
        cal(right[t])

        # 부모 노드가 연산자면 계산
        if tree[t] in not_num:
            # 어짜피 아래부터 계산하기 때문에 자식 노드가 숫자인지 확인 할 필요 없음
            # if is_num(left[t], right[t]):
            if tree[t] == "/":
                num = tree[left[t]] / tree[right[t]]
            elif tree[t] == "*":
                num = tree[left[t]] * tree[right[t]]
            elif tree[t] == "+":
                num = tree[left[t]] + tree[right[t]]
            elif tree[t] == "-":
                num = tree[left[t]] - tree[right[t]]

            tree[t] = num


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    not_num = ("-", "+", "*", "/")  # 연산자인지 확인하기 위해 선언

    for i in range(1, N + 1):
        dummy = input().split()
        dummy_len = len(dummy)
        if dummy[1] in not_num:     # 입력값이 연산자면 그냥 넣기
            tree[i] = dummy[1]
        else:
            tree[i] = int(dummy[1]) # 입력값이 연산자가 아니면 형변환

        # 자식노드가 있다면 길이별로 left, right 배열에 할당
        if dummy_len == 3:
            left[i] = int(dummy[2])
        elif dummy_len == 4:
            left[i] = int(dummy[2])
            right[i] = int(dummy[3])

    cal(1)  # 계산 함수 호출

    print(f"#{tc} {int(tree[1])}")
