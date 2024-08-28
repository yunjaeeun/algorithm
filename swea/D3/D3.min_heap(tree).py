'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40

'''
def make_min_heap(t):
    global last_idx
    last_idx += 1
    min_heap[last_idx] = t
    child = last_idx
    parent = child // 2

    # 부모 노드를 계속 올라가며 최소값으로 변경해줌
    while parent >= 1 and min_heap[parent] > min_heap[child]:
        temp = min_heap[parent]
        min_heap[parent] = min_heap[child]
        min_heap[child] = temp
        child = parent
        parent = child // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_heap = [0] * (N + 1)

    last_idx = 0

    for num in arr:
        make_min_heap(num)

    result = 0
    while last_idx > 0:
        last_idx //= 2
        result += min_heap[last_idx]
    print(f"#{tc} {result}")
