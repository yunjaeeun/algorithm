def selection_sort(lst, N):
    # lst : 정렬 대상
    # N : 정렬 대상 길이(원소 개수)
    for i in range(N - 1):
        # i번 인덱스의 자리 주인을 찾을건데
        # 남은 원소들 중에서 제일 작은 원소를 찾을것이다.
        min_idx = i
        for j in range(i + 1, N):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

lst = [5, 2, 1, 9, 4, 3]
selection_sort(lst,len(lst))

print(lst)