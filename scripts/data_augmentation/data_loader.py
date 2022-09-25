import os
import sys
import glob

import cv2
import numpy as np

# read yolov5 dataset
def read_files(dir_path: str = "data/yolov5/train"):
    image_dir = dir_path + "/images"
    image_paths = glob.glob(image_dir + "/*.jpg")

    label_dir = dir_path + "/labels"
    label_paths = glob.glob(label_dir + "/*.txt")

    image_paths.sort()
    label_paths.sort()

    return image_paths, label_paths