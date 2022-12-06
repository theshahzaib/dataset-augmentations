import Augmentation_backend as am
import Helpers_ as hp
import cv2
from helpers import *
import glob, os
import argparse
import math, random
# import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import PIL.Image
# import torch
# from torchvision import transforms
import shutil
from tqdm import tqdm

def augment_all_one(image, output_path, txt_path, image_name, aug_):

    if aug_ == 'brightness':
        image = am.brighten(image, brightness_coeff=0.3)

    if aug_ == 'darken':
        image = am.darken(image, darkness_coeff=0.1)

    if aug_ == 'add_shadow':
        image = am.add_shadow(image, no_of_shadows=2, shadow_dimension=8)

    if aug_ == 'add_rain':
        image = am.add_rain(image, rain_type='heavy', slant=20)

    if aug_ == 'add_fog':
        image = am.add_fog(image, fog_coeff=0.3)

    if aug_ == 'add_gravel':
        image = am.add_gravel(image, rectangular_roi=(700, 550, 1280, 720), no_of_patches=20)

    # if aug_ == 'add_sun_flare':
    #     image = am.add_sun_flare(image, flare_center=(100, 100), angle= -(math.pi)/4)

    # if aug_ == 'add_speed':
    #     image = am.add_speed(image, speed_coeff=0.9)

    if aug_ == 'add_autumn':
        image = am.add_autumn(image)

    if aug_ == 'hsv':
        image1 = image.copy()
        aug = iaa.imgcorruptlike.Saturate(severity=3)
        image = aug(image=image1)

    if aug_ == 'green':
        img = image
        row, col, plane = img.shape
        temp = np.zeros((row, col, plane), np.uint8)
        temp[:, :, 1] = img[:, :, 1]
        image = temp.copy()

    if aug_ == 'blue':
        img = image
        row, col, plane = img.shape
        temp = np.zeros((row, col, plane), np.uint8)
        temp[:, :, 1] = img[:, :, 0]
        image = temp.copy()

    if aug_ == 'red':
        img = image
        row, col, plane = img.shape
        temp = np.zeros((row, col, plane), np.uint8)
        temp[:, :, 1] = img[:, :, 2]
        image = temp.copy()

    if aug_ =='add_blur':
        aug = iaa.imgcorruptlike.MotionBlur(severity=5)
        image = aug(image=image)

    if aug_ == 'hue':
        aug = iaa.AddToHue((-50, 50))
        image = aug(image=image)

    if aug_ == 'gaussian_noise':
        aug = iaa.imgcorruptlike.GaussianNoise(severity=5)
        image = aug(image=image)

    if aug_ == 'linearcontrast':
        aug = iaa.LinearContrast((0.75, 1.5))
        image = aug(image=image)

    if aug_ == 'change_temperature':
        aug = iaa.ChangeColorTemperature((1100, 10000))
        image = aug(image=image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(output_path + aug_ + '_' + image_name, image)
    # print(image_name)
    name = image_name[:-4]
    # print(name)
    shutil.copy(txt_path, output_path + name + '.txt')
    # shutil.copy(txt_path, output_path + aug_ + '_' + name + '.txt')
    os.rename(output_path + name + '.txt', output_path + aug_ + '_' + name + '.txt')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--images', type=str, default='dataset/', help='path to input images')
    # parser.add_argument('--labels', type=str, default='', help='path to input images')
    parser.add_argument('--type', type=str, default= 'all' , help='augmentation type')
    parser.add_argument('--ext', type=str, default='jpg', help='image extension')
    args = parser.parse_args()
    
    aug_types = [ 'brightness', 'darken', 'add_shadow', 'add_rain', 'add_graval', 'add_speed', 'hsv', 'green', 'blue',
                 'red', 'hue', 'linearconstrast', 'gaussian_noise','change', 'add_blur', 'add_sun_flare', 'add_fog',
                 'add_autumn', 'change_temperature' ]

    if args.type == 'all':
        aug_type_list = aug_types
    elif args.type != 'all':
        aug_type_list = [args.type]
    else:
        print(f'Invalid argument: "{args.type}" augmentation type should be from the list "{aug_types}"')

    
    images_list = glob.glob(args.images + '*.{}'.format(args.ext))
    # print(images_list)

    # remove folder named 'augmented_images' if it exists
    if os.path.exists('augmented_images'):
        shutil.rmtree('augmented_images')
    
    # print('Augmenting images...')
    for aug_ in tqdm(aug_type_list, desc='Augmenting images', position=0):

        output_path = 'augmented_images/' + aug_ + '/'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # print(f'Augmenting images with {aug_}...')
        for img_path in tqdm(images_list, desc=f'Augmenting images with {aug_}', position=1, leave=True):
            # print(img_path)
            image_name = os.path.basename(img_path)
            txt_name = image_name[:-4]
            txt_path = args.images + txt_name + '.txt'
            image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

            augment_all_one(image, output_path, txt_path, image_name, aug_)
            # print('Augmented image saved to {}'.format(output_path))

    
