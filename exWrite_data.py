f = open("240828.txt", 'w')
f.close()



f = open("C:/Users/human/Desktop/수업필기/240828.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
