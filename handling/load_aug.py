import imgaug.augmenters as iaa
import cv2

# define the image augmentation aug non-geometric
def _load_augmentation_aug_non_geometric():
    return iaa.Sequential([
        iaa.Sometimes(0.3, iaa.Multiply((0.5, 1.5), per_channel=0.5)),
        iaa.Sometimes(0.2, iaa.JpegCompression(compression=(70, 99))),
        iaa.Sometimes(0.2, iaa.GaussianBlur(sigma=(0, 3.0))),
        iaa.Sometimes(0.2, iaa.MotionBlur(k=15, angle=[-45, 45])),
        iaa.Sometimes(0.2, iaa.MultiplyHue((0.5, 1.5))),
        iaa.Sometimes(0.2, iaa.MultiplySaturation((0.5, 1.5))),
        iaa.Sometimes(0.34, iaa.MultiplyHueAndSaturation((0.5, 1.5), per_channel=True)),
        iaa.Sometimes(0.34, iaa.Grayscale(alpha=(0.0, 1.0))),
        # iaa.Sometimes(0.2, iaa.ChangeColorTemperature((1100, 10000))),
        iaa.Sometimes(0.1, iaa.GammaContrast((0.5, 2.0))),
        iaa.Sometimes(0.2, iaa.SigmoidContrast(gain=(3, 10), cutoff=(0.4, 0.6))),
        iaa.Sometimes(0.1, iaa.CLAHE()),
        iaa.Sometimes(0.1, iaa.HistogramEqualization()),
        iaa.Sometimes(0.2, iaa.LinearContrast((0.5, 2.0), per_channel=0.5)),
        iaa.Sometimes(0.1, iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)))
    ])

# define the image augmentation aug geometric
def _load_augmentation_aug_geometric():
    return iaa.OneOf([
        iaa.Sequential([iaa.Fliplr(0.5),iaa.Resize(size=(0.8, 1.2)), iaa.Affine(scale=(0.8, 1.2))]),
        iaa.CropAndPad(percent=(0.1),
                       pad_mode='constant',
                       pad_cval=(0, 255)),
        iaa.Crop(percent=(0.01, 0.1)),
        iaa.Sequential([
            iaa.Affine(
                    # scale images to 80-120% of their size,
                    # individually per axis
                    scale={"x": (0.8,1.2 ), "y": (0.8, 1.2)},
                    # translate by -20 to +20 percent (per axis)
                    translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
                    rotate=(-10, 10),  # rotate by -10 to +10 degrees
            ),
            iaa.Sometimes(0.3, iaa.Crop( percent=(0.01, 0.1)))])
    ]) 

# define the image augmentation aug mix
def _load_augmentation_aug():
    return iaa.OneOf([
        iaa.Sequential([
            iaa.Fliplr(0.5), # horizontal flips / l???t ngang
            iaa.Resize(size=(0.8, 1.2)), # resize / thay ?????i k??ch th?????c
            iaa.Affine(
                scale=(0.8, 1.2), # scale images to 80-120% of their size,
                translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)}, # translate by -10 to +10 percent (per axis)
                rotate=(-10, 10), # rotate by -10 to +10 degrees
                shear=(-10, 10), # shear by -10 to +10 degrees
                ),
            iaa.LinearContrast((0.8, 1.3), per_channel=0.3), # improve or worsen the contrast / c???i thi???n ho???c l??m x???u ??i ????? t????ng ph???n
            iaa.Multiply((0.8, 1.3), per_channel=0.3), # change brightness of images (80-120% of original value) / thay ?????i ????? s??ng c???a h??nh ???nh (80-120% gi?? tr??? ban ?????u)
            iaa.GaussianBlur(sigma=(0, 1.5)), # blur images with a sigma of 0 to 3.0 / l??m m??? h??nh ???nh v???i sigma t??? 0 ?????n 1.0
            iaa.AdditiveGaussianNoise(scale=(0.0, 0.03*255), per_channel=0.3), # add gaussian noise to images / th??m ????? nhi???u gaussian v??o h??nh ???nh
            ]),
        _load_augmentation_aug_geometric()          
    ])