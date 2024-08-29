'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''
T = int(input())        # 테스트 케이스의 수

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())     # K = 이동가능 거리, N = 가야할 거리, M = 정류장 수
    arr = list(map(int, input().split()))   # 정류장의 위치
    STATIONS = [0] * N
    STATIONS.append(N)                      # 종료 조건 설정
    result = 0

    for value in arr:
        # 각 인덱스에 정류장 까지의 거리를 일치시켜서 저장
        # ex[1, 3, 5] -> [0, 1, 0, 3, 0, 5]
        STATIONS[value] += value
    current_position = 0                    # 현재 위치
    station_count = 0                       # 방문횟수
    while current_position != N:            # 현재 위치가 종료지점일때까지 반복
        # 현재 위치 ~ 이동가능한 거리 내부의 최댓값
        max_position = max(STATIONS[current_position + 1:current_position + K + 1])

        if max_position != 0 and max_position != N: # 최대값이 0이 아니고 종료지점에 도달하지 않았으면
            station_count += 1                      # 방문횟수 + 1
            current_position = max_position         # 현위치 갱신
        elif max_position == N:
            break
        else:                                       # 최대값이 0이면 방문횟수를 0으로 초기화 후 탈출
            station_count = 0
            break

    print(f"#{tc} {station_count}")

