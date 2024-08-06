'''

3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

'''


def find_reverse_string(str_len, reverse_str_len, str_arr):
    i = 0                           # 세로열 인덱스
    start = 0                       # 문자열 탐색 시작위치
    end = reverse_str_len           # 문자열 탐색 종료위치

    # 가로열 탐색
    while i < str_len:              # 세로열 탐색이 끝날때까지 ex) N = 10, while = 0 ~ 9
        while end <= str_len:       # 슬라이싱을 사용하기 때문에 이하일때까지 ex M = 10,  arr[0:M]
            string = "".join(str_arr[i][start:end])     # arr = [h,e,l,l,o] string = hello
            reverse_string = string[::-1]

            # 세로열 탐색
            vertical_string = ""

            # 세로열은 슬라이싱이 불가능해 반복문으로 작성
            for j in range(start, end):
                vertical_string += arr[j][i]
            reverse_vertical_string = vertical_string[::-1]

            if string == reverse_string:
                return string
            if vertical_string == reverse_vertical_string:
                return vertical_string
            start += 1
            end += 1
        i += 1
        start = 0
        end = reverse_str_len


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 테스트 케이스의 길이, M = 회문의 길이

    arr = [list(input()) for _ in range(N)]

    result = find_reverse_string(N, M, arr)

    print(f"#{tc} {result}")
