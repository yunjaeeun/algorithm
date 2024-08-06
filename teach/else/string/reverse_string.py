# 슬라이싱 사용
s = "Reverse this strings" 
print(s[::-1]) # sgnirts siht esreveR

# for문 사용
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="") # sgnirts siht esreveR

print()
# list 사용
s = list(s)
s.reverse()
s = "".join(s)
print(s) # sgnirts siht esreveR