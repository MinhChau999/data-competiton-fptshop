fNoMask = open('FileNoMask.txt','r+')
fFalseMask = open('FileFalseMask.txt','r+')

text1 = fNoMask.readlines()
text2 = fFalseMask.readlines()

for i in text1:
    i = i.replace('\n','')
    f = open(i,'r')
    text = f.readlines()
    for k in range(1,3):
        path = i.replace(".txt","") + "_1_" + str(k) + ".txt"
        f1 = open(path,'w+')
        for j in text:
            f1.write(j)
            print(j)
        f1.close()
    f.close()

for i in text2:
    i = i.replace('\n','')
    f = open(i,'r')
    text = f.readlines()
    for k in range(1,11):
        path = i.replace(".txt","") + "_1_" + str(k) + ".txt"
        f1 = open(path,'w+')
        for j in text:
            f1.write(j)
            print(j)
        f1.close()
    f.close()

fNoMask.close()
fFalseMask.close()