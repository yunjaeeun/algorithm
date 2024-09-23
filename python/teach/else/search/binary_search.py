def binary_search(lst, N, key):
    # lst : 검색 대상
    # N : 검색 대상 길이
    # key : 내가 찾는 값
    start = 0  # 검색 시작 위치(인덱스)
    end = N - 1  # 검색 끝 위치(인덱스)

    while start <= end:
        # start가 end 이하이면 재대로 된 범위 => 검색 계속
        # start와 end가 교차 되어버리면 => 범위 잘못 => 검색 실패
        mid = (start + end) // 2

        if lst[mid] == key:
            # 가운데 찍었는데 원하는 값을 찾음, 검색 성공
            # 찾은 값의 위치 반환
            return mid
        elif lst[mid] > key:
            # 가운데 원하는 값보다 크다 => 오른쪽엔 없음
            # 검색 범위를 가운데 기준 왼쪽으로 좁힌다.
            end = mid - 1
        else:
            # 가운데 값이 원하는 값보다 작다 => 오른쪽엔 없다
            # 검색 범위를 가운데 기준 오른쪽으로 좁힌다.
            start = mid + 1

    # 반복문 종료 => 원하는 값을 찾지 못함.
    return -1


numbers = [2, 3, 5, 7, 8, 9, 11]

print(binary_search(numbers, len(numbers), 9))
print(binary_search(numbers, len(numbers), 6))
