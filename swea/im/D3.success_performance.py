'''
4
11111
09
110011
1

'''
T = int(input())

for tc in range(1, T + 1):
    peoples = list(map(int, input()))

    result = 0
    clap_count = peoples[0]

    for i in range(1, len(peoples)):
        if peoples[i] != 0 and clap_count < i:  # 박수 치는 사람이 0명이면 계산할 필요가 없음
            additional_people = i - clap_count  # 고용할 사람의 횟수 -> 필요한 사람 - 현재 치고 있는 사람
            result += additional_people
            clap_count += additional_people + peoples[i]
        else:
            clap_count += peoples[i]

    print(f"#{tc} {result}")
