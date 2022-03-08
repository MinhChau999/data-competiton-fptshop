import cv2
import glob
from mix_up import mix_up

# 1. Load dataset
images = []
images_path = glob.glob("images/*.jpg")
lables_path = glob.glob("labels/*.txt")
for i in range(len(images_path)):
    images.append(cv2.imread(images_path[i]))
    label = 0 # open(labels_path[i]).read()

ds_one = images[0], 0
ds_two = images[1], 1

image_mu, label_mu = mix_up(ds_one, ds_two)

print(image_mu.shape, label_mu)
