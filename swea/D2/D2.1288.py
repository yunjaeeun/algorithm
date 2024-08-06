T = int(input())

for i in range(T):
    num = int(input())
    arr = set()
    result = 0

    while len(arr) < 10:
        result += 1

        sheep = num * result
        
        for char in str(sheep):
            arr.add(char)
            
    print(f"#{i + 1} {sheep}")