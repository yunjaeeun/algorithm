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


def h_to_b(hex_value):
    result = ""
    for char in hex_value:
        result += bi_dict[char]

    return result


# def valid_code(code):
#     code_len = len(code)
#     code_ratio = []
#     total_code = []
#     total_cnt = 0
#     for i in range(code_len):
#         # 처음에 오는 0은 배제
#         if code[i] == "1":
#             part_len = 0
#             cnt = 0
#             add_cnt = 0
#             current_code = code[i]
#             current_idx = i
#             # 찾은 위치부터 코드 탐색 시작
#             start_idx = i
#             while current_idx < code_len:
#                 # 만약 같으면 길이 증가
#                 if code[current_idx] == current_code:
#                     cnt += 1
#                     current_idx += 1
#                 # 다른걸 만나면 비율 추가, 길이 초기화
#                 else:
#                     code_ratio.append(cnt)
#                     add_cnt += 1
#                     part_len += cnt
#                     cnt = 0
#                     current_code = code[current_idx]
#                 # 비율 3개 저장했으면 일치하는지 확인
#                 if add_cnt == 3 and part_len == 7:
#                     rate_1, rate_2, rate_3 = code_ratio
#                     while rate_1 > 0:
#                         if rate_1 % 1 == 0 and rate_2 % 1 == 0 and rate_3 % 1 == 0:
#                             now_ratio = ""
#                             now_ratio += str(int(rate_1))
#                             now_ratio += str(int(rate_2))
#                             now_ratio += str(int(rate_3))
#
#                             # 일치하는 비율이 있다면
#                             if now_ratio in decryption_dict:
#                                 total_code.append(decryption_dict[now_ratio])
#                                 total_cnt += 1
#                                 code_ratio.clear()
#                                 add_cnt = 0
#                                 start_idx = current_idx
#                                 part_len = 0
#                                 break
#                             # 일정한 비율을 확인하기 위해 2씩 나누기
#                             rate_1 /= 2
#                             rate_2 /= 2
#                             rate_3 /= 2
#                         # 비율이 존재하지 않으면
#                         else:
#                             add_cnt = 0
#                             code_ratio.clear()
#                             current_idx = start_idx + 1     # 다음 위치부터 탐색
#                             part_len = 0
#                             break
#                 elif part_len != 7 and add_cnt == 3:
#                     current_idx = current_idx - part_len
#                     add_cnt = 0
#                     part_len = 0
#     return total_code

def valid_code(code):
    code_len = len(code)
    # 앞의 0 배제
    for i in range(code_len):
        if code[i] == "1":
            start_idx = i
            break


T = int(input())
bi_dict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
           "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
decryption_dict = {"211": 0, "221": 1, "122": 2, "411": 3, "132": 4, "231": 5, "114": 6, "312": 7, "213": 8, "112": 9}

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()[:M + 1]) for _ in range(N)]

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
                b_value = h_to_b(h_value)
                result = valid_code(b_value)
                print(result)
                current_j = start - 1
