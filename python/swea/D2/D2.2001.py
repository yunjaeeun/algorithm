T = int(input())  # 테스트 케이스의 수 입력
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    N, M = map(int, input().split())  # N은 행렬의 크기, M은 부분 배열의 크기
    lst = [list(map(int, input().split())) for _ in range(N)]  # N x N 행렬 입력

    mx = 0  # 최대 합을 저장할 변수 초기화
    for i in range(N - M + 1):  # 부분 배열의 시작 행 인덱스
        for j in range(N - M + 1):  # 부분 배열의 시작 열 인덱스
            tmp_sum = 0  # 현재 부분 배열의 합을 저장할 변수 초기화
            for k in range(M):  # 부분 배열의 각 행을 순회
                tmp_sum += sum(lst[i + k][j:j + M])  # 부분 배열의 한 행의 합을 tmp_sum에 더함
            mx = max(mx, tmp_sum)  # 현재까지의 최대 합과 비교하여 더 큰 값을 mx에 저장
    print(f"#{tc} {mx}")  # 결과 출력