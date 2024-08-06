T = int(input())

for i in range(T):
    N = int(input())
    result = [[1]]
    
    for j in range(N - 1):
        row = [1]

        for k in range(len(result) - 1):
            row.append(result[j][k] + result[j][k + 1])
        
        row.append(1)
        result.append(row)

    print(f"#{i + 1}")
    for l in range(len(result)):
        print(" ".join(map(str, result[l])))
