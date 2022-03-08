# mở file cần sửa
fNoMask = open('FileNoMaskVal.txt','r+')
fFalseMask = open('FileFalseMaskVal.txt','r+')

pNoMask = open('PathNoMaskVal.txt','w+')
pFalseMask = open('PathFalseMaskVal.txt','w+')

# sửa lại đường dẫn
text1 = fNoMask.readlines()
text2 = fFalseMask.readlines()
for i in text1:
    # viết lại đường dẫn
    i = i.replace('labels/','images/')
    i = i.replace('txt','jpg')
    pNoMask.write(i)
for i in text2:
    i = i.replace('labels/','images/')
    i = i.replace('txt','jpg')
    pFalseMask.write(i)

fNoMask.close()
fFalseMask.close()
pNoMask.close()
pFalseMask.close()
