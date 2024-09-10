'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

'''

T = int(input())

result_lst = []


def find_parent(child):
    if parents[child] == child:  # 지금 자신과 부모가 같다면 본인 리턴
        return child

    return find_parent(parents[child])  # 같지 않다면 부모를 찾아서 리턴


def union(p_1, p_2):
    # people_1, people_2 = p_1, p_2의 부모
    people_1 = find_parent(p_1)
    people_2 = find_parent(p_2)

    # 일관된 기준으로 저장하기 위해 더 작은 번호를 부모로 설정
    parent = min(people_1, people_2)
    child = max(people_1, people_2)

    # 부모 정보를 탐색하며 자식을 부모로 가진 집합을 부모 집합으로 합치기
    for i in range(N + 1):
        if parents[i] == child:
            parents[i] = parent


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 거주하는 사람수, M: 관계수
    parents = [i for i in range(N + 1)]  # 집합의 부모를 저장할 배열

    for _ in range(M):
        p_1, p_2 = map(int, input().split())  # p_1, p_2 = 서로 알고있는 사람의 번호
        union(p_1, p_2)

    result = set()
    # 부모를 전체 배열을 순회하며 추가(set이기 때문에 중복은 저장이 되지 않음)
    for value in parents:
        result.add(value)

    print(f"#{tc} {len(result) - 1}")
