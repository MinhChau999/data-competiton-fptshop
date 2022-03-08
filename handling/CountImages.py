import glob

text_path_val_txt = glob.glob("labels/val/*.txt")
text_path_train_txt = glob.glob("labels/train/*.txt")
text_path_train_jpg = glob.glob("images/train/*.jpg")
text_path_val_jpg = glob.glob("images/val/*.jpg")

print("Number of images in train: ", len(text_path_train_jpg))
print("Number of images in val: ", len(text_path_val_jpg))
print("Number of labels in train: ", len(text_path_train_txt))
print("Number of labels in val: ", len(text_path_val_txt))