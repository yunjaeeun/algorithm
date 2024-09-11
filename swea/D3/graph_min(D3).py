'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''


def find_min(start, cnt):
    global result

    if cnt > result:  # 탐색 중에 이미 최솟값을 넘었다면(가지치기)
        return

    if start == N:  # 도착지점에 도착했다면(종료조건)
        if result > cnt:  # 최솟값 비교후 갱신
            result = cnt
        return

    for value in arr[start]:    # 현재 연결지점에서 길이 있다면 탐색(재귀 호출)
        find_min(value[0], cnt + value[1])


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N: 마지막 연결지점, E: 도로의 개수

    arr = [[] for _ in range(E)]  # 연결리스트

    for i in range(E):
        s, e, v = map(int, input().split())
        arr[s].append((e, v))  # 도착지점, 가중치 저장

    result = 1e9  # 최댓값 설정(넉넉하게)

    find_min(0, 0)
    print(f"#{tc} {result}")
