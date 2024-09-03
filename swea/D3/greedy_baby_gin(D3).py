'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

'''


def is_baby_gin(cards):
    card_ctn = [0] * 10  # 카드의 등장 횟수
    for card in cards:
        card_ctn[card] += 1  # 등장횟수만큼 + 1

    for ctn in card_ctn:  # 3번 이상 등장한게 있다면 승리조건 달성(triplet)
        if ctn >= 3:
            return True

    for i in range(8):
        # run 조건 달성
        if card_ctn[i] > 0 and card_ctn[i + 1] > 0 and card_ctn[i + 2] > 0:
            return True

    # 둘 다 아니라면 실패
    return False


def find_winner():
    p1 = []
    p2 = []
    p1_win = False
    p2_win = False
    for i in range(6):
        # 플레이어가 카드를 한장씩 나눠받음
        p1.append(arr[i * 2])
        p2.append(arr[i * 2 + 1])

        if is_baby_gin(p1):  # 승리조건 달성 확인 함수 호출
            p1_win = True
        elif is_baby_gin(p2):  # 승리조건 달성 확인 함수 호출
            p2_win = True

        if p1_win and p2_win:  # 둘 다 True면 무승부
            return 0
        elif p1_win:  # 둘 중 하나면 True면 승리한 플레이어 리턴
            return 1
        elif p2_win:
            return 2

    return 0  # 둘 다 승리조건을 달성하지 못하면


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = find_winner()

    print(f"#{tc} {result}")
