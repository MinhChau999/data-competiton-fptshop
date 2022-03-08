import imgaug.augmenters as iaa
import cv2
import glob
from load_aug import _load_augmentation_aug

# 1. Load dataset
images = []
images_path = glob.glob("images/*.jpg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)
# 2. Image Augmentation
augmentation = _load_augmentation_aug()
while True:
    augmented_images = augmentation(images=images)
    # 3. Show image
    for im in augmented_images:
        cv2.imshow("Image", im)
        cv2.waitKey(0)


# 4. Save image
# for i in range(0,len(augmented_images)):
#     print(i)
#     cv2.imwrite("hinh/Grayscale"+ str(images_path[i].replace('images\\', '')), augmented_images[i])