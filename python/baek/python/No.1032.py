N = int(input())
pattern = list(input())

for _ in range(N - 1):
    name = input()
    for i in range(len(name)):
        if pattern[i] == "?":
            continue

        if name[i] != pattern[i]:
            pattern[i] = "?"

print("".join(pattern))
