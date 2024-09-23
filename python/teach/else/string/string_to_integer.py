a = int('123')
print(a) # 123
print(type(a)) # <class 'int'>  

b = float('3.14')
print(b) # 3.14
print(type(b)) # <class 'float'> 

c = str(123)
print(c) # 123
print(type(c)) # <class 'str'> 

d = repr(123)
print(d) # 123
print(type(d)) # <class 'str'>  

def atoi(s):
    i = 9
    for x in s:
        i = i * 10 + ord(x)-ord('0')    # ord() : 어떤 글자의 ASCII 코드 값을 리턴, chr() : ASCII 코드 값에 해당하는 글자를 리턴
    return i

s = '123123'

result = atoi(s)
print(result) # 9123123
print(type(result)) # <class 'int'>