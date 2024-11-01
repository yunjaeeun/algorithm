N, M = map(int, input().split())

my_dict = {}
for _ in range(N):
    link, pwd = input().split()
    my_dict[link] = pwd
    
for _ in range(M):
    print(my_dict[input()])