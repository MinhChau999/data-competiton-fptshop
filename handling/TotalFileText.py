import glob

# Convert many file .txt to 1 file .txt
f = open('totalTxt.txt','w+')
f1 = open('totalTxtVal.txt','w+')
txt_path_train = glob.glob("labels/train/*.txt")
print(len(txt_path_train))
txt_path_val = glob.glob("labels/val/*.txt")
print(len(txt_path_val))
for text_path in txt_path_train:
    fileRead=open(text_path,'r')
    text = fileRead.readlines()
    f.writelines(text)
    fileRead.close()

for text_path in txt_path_val:
    fileRead=open(text_path,'r')
    text = fileRead.readlines()
    f1.writelines(text)
    fileRead.close()
f1.close()
f.close()
