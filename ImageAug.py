import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt
from skimage import data
from skimage.transform import rescale
import warnings
import os
import cv2

warnings.filterwarnings("ignore")

count = 0

path_image = --path to original image folder--
path_dest = --path to destination folder--

class ImgAug:
    image_list =[]

    def __init__(self):
        for filename in os.listdir(path_image):
            image = cv2.imread(os.path.join(path_image, filename))
            self.image_list.append(image)

    def contrast(self):
            for image in self.image_list:
                v_min, v_max = np.percentile(images, (0.2, 98))
                better_contrast = exposure.rescale_intensity(image,in_range=(v_min, v_max))
                cv2.imwrite(
                  --path_dest-- + str(
                    filename), better_contrast)

    def gamma(self):
        for image in self.image_list:
            adjusted_gamma_image = exposure.adjust_gamma(image, gamma=0.6, gain=0.9)
            cv2.imwrite(
                --path_dest-- + str(
                    filename), adjusted_gamma_image)

    def log(self):
        for image in self.image_list:
            log_correction_image = exposure.adjust_log(image)
            cv2.imwrite(
                --path_dest-- + str(
                    filename), log_correction_image)

    def sigmoid(self):
        for image in self.image_list:
            sigmoid_correction_image = exposure.adjust_sigmoid(image)
            cv2.imwrite(
                --path_dest-- + str(
                    filename), sigmoid_correction_image)

