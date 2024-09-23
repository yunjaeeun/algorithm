'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

'''


def my_func(c_arr):
    isEnd = False
    for i in range(1, len(c_arr)):
        if c_arr[i - 1] != c_arr[i]:
            isEnd = True
        else:
            isEnd = False
            break
    if isEnd or len(c_arr) == 1:
        return
    else:
        for i in range(len(c_arr) - 1):
            if c_arr[i] == c_arr[i + 1]:
                c_arr.pop(i)
                c_arr.pop(i)
                break
        my_func(c_arr)


T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())

    my_func(str1)

    print(f"#{tc} {len(str1)}")
