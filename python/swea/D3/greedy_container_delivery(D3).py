'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

'''
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 컨테이너 수, M = 트럭 수
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()

    weight = 0
    for truck in trucks:
        max_weight = 0
        idx = 0
        for j in range(N):
            if max_weight < containers[j] <= truck:
                max_weight = containers[j]
                idx = j

        if max_weight > 0:
            weight += max_weight
            containers[idx] = 0

    print(f"#{tc} {weight}")



