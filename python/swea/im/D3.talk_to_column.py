'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx

'''


def is_valid(cj, length):
    return 0 <= cj < length


T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    result = ""

    max_len = 0         # 테스트 케이스의 길이는 5줄로 고정이지만 문자열의 길이는 1 ~ 15이므로 가장 긴 문자열의 길이를 찾아줌
    for i in range(5):
        c_len = len(arr[i])
        if c_len > max_len:
            max_len = c_len

    for j in range(max_len):
        for i in range(5):
            current_length = len(arr[i])    # 현재 문자열의 길이

            if is_valid(j, current_length): # 넘어가지 않으면 문자열에 추가
                result += arr[i][j]

    print(f"#{tc} {result}")
