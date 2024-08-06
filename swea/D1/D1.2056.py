t = int(input())

for i in range(t):
    date = int(input())
    str_date = str(date)
    # 연도가 0000이면 -1 출력
    if str_date[0:4] == "0000":
        print(-1)
    
    # 월이 00이면 -1 출력
    elif str_date[4:6] == "00":
        print(-1)
    
    # 일이 00이면 -1 출력
    elif str_date[6:] == "00":
        print(-1)

    elif str_date[4:6] == "00" and date[6:0] > 28:
        print(-1)    
    else:
        arr = [str_date[0:4], str_date[4:6], str_date[6:]]

        print("#{0} {1}/{2}/{3}".format(i + 1, arr[0], arr[1], arr[2]))