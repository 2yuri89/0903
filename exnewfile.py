f = open("새파일.txt", 'w')
f.close()

f = open("C:/Work/0903/새파일2.txt", 'w')
f.close()

f = open("C:/Work/0903/새파일2.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("C:/Work/0903/새파일2.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/Work/0903/새파일2.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()