# Image augmentation
import imgaug.augmenters as iaa
import cv2
from load_aug import _load_augmentation_aug


# 1. Load dataset
images = []
images_path_txt = open("PathFalseMask.txt",'r')
images_path = images_path_txt.readlines()
for img_path in images_path:
    img = cv2.imread(img_path.split('\n')[0])
    images.append(img)

# 2. Create augmentation object
augmentation = _load_augmentation_aug()
augmented_images = augmentation(images=images)  # images is a list of images

    
# 3. Save augmented images
for i in range(len(augmented_images)):
    images_path[i] = images_path[i].replace('\n','')
    images_path[i] = images_path[i].replace('images/train\\','')
    images_path[i] = images_path[i].replace('.jpg','')
    cv2.imwrite("non_geometric_false/" + images_path[i] + "_1.jpg",augmented_images[i])

images_path_txt.close()