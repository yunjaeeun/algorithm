t = int(input())

for i in range(t):
    a, b = map(int,input().split(" "))

    if a == b:
        print("#{0} =".format(i + 1))
    elif a > b:
        print("#{0} >".format(i + 1))
    else:
        print("#{0} <".format(i + 1))