T = int(input())

for i in range(T):
    test_num = int(input())
    students_score = list(map(int, input().split()))
    score_count = []

    result = 0

    for _ in range(101):
        score_count.append(0)
    

    for score in students_score:
        score_count[score] += 1
    
    max_count = max(score_count)
    
    print(score_count)
    print(max_count)

    arr = []
    for j in range(len(score_count)):
        if score_count[j] == max_count:
            arr.append(j)

    result = max(arr)

    print(f"#{test_num} {result}")
