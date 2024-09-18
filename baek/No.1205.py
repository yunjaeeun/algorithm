'''
3 90 10
100 90 80
10 1 10
10 9 8 7 6 5 4 3 2 1
10 1 10
10 9 8 7 6 5 4 3 3 0
0 0 50

'''
N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    if N == P and arr[-1] >= score:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if arr[i] <= score:
                result = i + 1
                break
        print(result)
