import glob

# Find image path have "False-Mask" and "No-Mask"
fNoMask = open('FileNoMaskVal.txt','w+')
fFalseMask = open('FileFalseMaskVal.txt','w+')
txt_path = glob.glob("labels/val/*.txt")
for text_path in txt_path:
    fileRead=open(text_path,'r')
    text = fileRead.readlines()
    for i in text:
        if(int(i[0])==0):
            fNoMask.write(text_path + "\n")
            print(text_path)
            break
        if(int(i[0])==2):
            fFalseMask.write(text_path+ "\n")
            print(text_path)
            break
    fileRead.close()
fFalseMask.close()
fNoMask.close()
