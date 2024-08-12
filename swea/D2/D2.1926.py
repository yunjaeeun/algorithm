# num = int(input())
#
# arr = ["3", "6", "9"]
#
# for i in range(1, num + 1):
#     rep = 0
#     for j in range(len(str(i))):
#         if str(i)[j] in arr:
#             rep += 1
#     if rep != 0:
#         print("-" * rep, end=" ")
#     else:
#         print(i, end=" ")

N = int(input())
# clap = ["3", "6", "9"]
clap = {"3", "6", "9"}      # set 타입의 in 연산자는 hash를 사용하기 때문에 더 빠르다.
for i in range(1, N + 1):
    str_num = str(i)
    count = 0
    for char in str_num:
        if char in clap:
            count += 1

    if count > 0:
        print("-" * count, end=" ")
    else:
        print(str_num, end=" ")

# 강사님 코드
# -의 개수는 3, 6, 9가 몇 개나 포함되어 있는지에 대해 결정
def check_369(number):
    count = 0
    # 숫자를 문자로 바꾸고
    # 바뀐 문자를 한 글짜식 확인하여 3, 6, 9인지 체크
    # 만약에 36 이라면 3, 6 2개가 포함되어 있기 떄문에 -- 두개가 나와야 한다.
    for char in str(number):
        # print(char)
        if char in ["3", "6", "9"]:  # 문자형이기 때문에 반드시 문자형으로 비교
            count += 1
    if count != 0:
        return "-" * count
    else:
        return str(number)      # join은 문자열 메서드이기 때문에 str로 형변환 필요
# N : 입력 최대 값
N = int(input())        # range에 사용해야 하기 때문에 정수로 형변환
arr = []                # 빈 배열에 결과를 담아서 join으로 한 줄로 표현
for number in range(1, N + 1):
    # print(number)       # 숫자로 접근을 하게 되면 어려워 진다.
                        # 우리가 봣을때 바로 확인할 수 있는 이유는
                        # 문자로 숫자를 생각하기 때문임 숫자형 => 문자로 형변환
                        # 문자열이 되면서 문자열의 특징으로 3, 6, 9를 판별할 수 잇음
    result = check_369(number)
    arr.append(result)

print(" ".join(arr))
