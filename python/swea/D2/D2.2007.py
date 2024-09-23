T = int(input())

for i in range(T):
    string = input()

    pattern = ""

    num = 1
    while num * 2 < len(string):

        str1 = string[:num]
        str2 = string[num:num*2]

        if str1 == str2:
            pattern = str1
            break

        num += 1
    print("#{0} {1}".format(i + 1, len(pattern)))
