str = input()

# ord() -> 아스키 코드로 변환
for i in range(len(str)):
    print(ord(str[i]) - 64, end=" ")
