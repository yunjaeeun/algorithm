import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N = 사람수, M = 소요시간, K = 가능한 갯수
    peoples = list(map(int, input().split()))
    peoples.sort()      # 오름차순으로 정렬해 손님이 시간대별로 순차적으로 오게 설정

    result = "Possible"

    for i in range(N):
        bread = (peoples[i] // M) * K       # (손님이 도착한 시간 // 빵을 만드는 소요 시간) * 만들 수 있는 빵의 갯수

        if bread < i + 1:   # 빵이 손님 수보다 적으면 불가능.
            result = "Impossible"
            break

    print(f"#{tc} {result}")
