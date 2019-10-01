a = open("a.txt",'r', encoding='utf-8')
b1 = open("b1.txt", 'w+', encoding='utf-8')
b2 = open("b2.txt", 'w+', encoding='utf-8')
cnt = 1
for i in a:
    if cnt % 2 == 0:
        b1.write(i.upper())
    else:
        b2.write(i.lower())
    cnt +=1

a.close()
b1.close()
b2.close()
