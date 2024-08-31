'''
2
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000
18 50
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000

'''
import sys
sys.stdin = open("input.txt", "r")

def h_to_b(hex_value):
    result = ""
    for char in hex_value:
        result += bi_dict[char]

    return result


def valid_start():
    for i in range(N):
        current_j = M - 1
        end = 0
        start = 0
        while current_j >= 0:
            if arr[i][current_j] == "0":
                current_j -= 1

            else:
                end = current_j
                # 길이 체크
                for j in range(current_j - 1, -1, -1):
                    if arr[i][j] == "0":
                        start = j
                        break

                h_value = arr[i][start + 1:end + 1]
                b_value = h_to_b(h_value)+"00000"
                result = valid_code(b_value)
                test = 0
                if result:
                    test = is_code(result)
                if test:
                    return test
                current_j = start - 1
    return 0


def valid_code(code):
    secret_code = []
    code_len = len(code)
    current_idx = 0
    code_ratio = []
    while current_idx < code_len:  # 전체 탐색
        if len(secret_code) == 8:
            return secret_code
        if code[current_idx] == "1":  # 비밀 코드의 시작은 항상 1부터 시작임
            ctn = 0  # 코드가 차지하는 칸수
            valid_idx = current_idx  # 탐색할 인덱스
            current_code = code[current_idx]  # 현재 코드 1 or 0
            while valid_idx < code_len and len(code_ratio) < 3:  # 앞의 0은 배제하므로 3개가 채워질 때 까지 반복
                if current_code == code[valid_idx]:  # 이전것과 같다면
                    ctn += 1  # 카운트 +1
                    valid_idx += 1  # 탐색 인덱스 +1
                elif current_code != code[valid_idx]:  # 다른걸 찾았다면
                    code_ratio.append(ctn)  # 현재 체크한 칸수 추가
                    current_code = code[valid_idx]  # 찾을 코드 변경
                    ctn = 0  # 차지하는 칸수 초기화

            if len(code_ratio) == 3:  # 비율이 3개가 되면 비율 비교
                rate_1, rate_2, rate_3 = code_ratio
                while rate_1 % 1 == 0 and rate_2 % 1 == 0 and rate_3 % 1 == 0:  # 소숫점이 없을때까지 반복
                    raito = str(int(rate_1)) + str(int(rate_2)) + str(int(rate_3))

                    if raito in decryption_dict:  # 복호화 표에 있다면
                        secret_code.append(decryption_dict[raito])  # 암호 등록
                        current_idx = valid_idx  # 다음 탐색범위 지정
                        break

                    rate_1 /= 2
                    rate_2 /= 2
                    rate_3 /= 2
                else:  # break가 되지 않으면 실행
                    current_idx += 1  # 다음 인덱스부터 탐색
                    code_ratio.clear()
                code_ratio.clear()
        else:
            current_idx += 1
    if len(secret_code) == 8:
        return secret_code
    else:
        return 0


def is_code(code_arr):
    odd_num = 0
    even_num = 0
    for i in range(8):
        if i % 2 == 0:
            odd_num += code_arr[i]
        else:
            even_num += code_arr[i]
    if ((odd_num * 3) + even_num) % 10 == 0:
        return odd_num + even_num
    else:
        return 0


T = int(input())
bi_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
           "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
decryption_dict = {"211": 0, "221": 1, "122": 2, "411": 3, "132": 4, "231": 5, "114": 6, "312": 7, "213": 8, "112": 9}

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()[:M + 1]) for _ in range(N)]

    a = valid_start()

    print(f"#{tc} {a}")
