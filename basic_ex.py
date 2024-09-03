print("Life is too shory\nYou need python")
print("-" * 30)
multiline = '''Life is too short
YOU
need python'''
print(multiline)

print("-" * 30)

head = "Python"
tail = " is fun!"
print(head + tail)
print((head + tail + "\n") * 3)
print(head[0:3])

print("-" * 30)

print("%10s" % "hi")
print("%-10sJame." % 'hi')
print("%0.4f" % 3.42134234)
print("%10.5f" % 3.42134234)

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'내년에는 {age + 1}입니다.')
print('나의 이름은 {name}입니다. 나이는 {age}입니다.') # 아하! f로 문자열 포매팅을 하지 않으면 변수가 문자 취급 당한다

print("-" * 30)


print("-" * 30)

i = 0
while i < 10:
    i = i + 1
print("i는 %d입니다." % i)

print("-" * 30)



print("-" * 30)
