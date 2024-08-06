s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 == s2)  # True
print(s1 == s3)  # False
print(s1 == s4)  # True
print(s1 == s5)  # True