f = open("c:/Work/0903/새파일2.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()





f = open("c:/Work/0903/새파일2.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()



print("========================")

f = open("c:/Work/0903/새파일2.txt", 'r')
data = f.read()
print(data)
f.close()



print("========================")

f = open("c:/Work/0903/새파일2.txt", 'r')
for line in f:
    print(line)
f.close()
print("-------------------")
f = open("c:/Work/0903/새파일2.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
