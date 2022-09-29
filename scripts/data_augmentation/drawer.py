import os
import sys
import glob
import shutil

import cv2
import numpy as np
import math

from data_loader import read_files

# calculate tree points
def calc_tree_points(root, length, theta, level):
    # root: [start_x, start_y]
    # theta: tree angle (degree)
    # level: recursive level
    sample = np.random.randn(2, 2)*5

    points = []
    root_end = (int(root[0]+length*math.cos(math.radians(theta))), int(root[1]+length*math.sin(math.radians(theta))))
    points.append([root, root_end])
    if level > 0:
        points.extend(calc_tree_points(root_end, (length+sample[0,0])*0.8, theta+20+sample[1,0], level-1))
        points.extend(calc_tree_points(root_end, (length+sample[0,1])*0.8, theta-20+sample[1,1], level-1))
    return points

# add lines to a image
def draw_lines(image, points):
    image_cp = image.copy()
    for point_pair in points:
        pair_start = (point_pair[0][0], image_cp.shape[0] + point_pair[0][1] * -1)
        pair_end = (point_pair[1][0], image_cp.shape[0] + point_pair[1][1] * -1)
        r = int(np.random.randint(0, 39, 1)[0])
        g = int(np.random.randint(70, 110, 1)[0])
        b = int(np.random.randint(10, 50, 1)[0])
        image_cp = cv2.line(image_cp, pair_start, pair_end, (r, g, b), thickness=1, lineType=cv2.LINE_AA)
    return image_cp

def draw_bubbles(image):
    bubble_num = 500
    height = image.shape[0]
    width = image.shape[1]
    x_points = np.random.randint(0, width, (bubble_num, 1))
    y_points = np.random.randint(0, height, (bubble_num, 1))
    center = np.concatenate([x_points, y_points], 1)
    axes_short = np.random.randint(1, 3, (bubble_num, 1))
    axes_long = np.random.randint(3, 5, (bubble_num, 1))
    axes = np.concatenate([axes_long, axes_short], 1)
    angle = np.random.normal(90, 6, bubble_num)
    colors = np.random.normal(170, 10, (bubble_num, 3)).astype(np.int32)
    colors.clip(0, 255)
    for i in range(bubble_num):
        color = (int(colors[i, 0]), int(colors[i, 2]), int(colors[i, 2]))
        image = cv2.ellipse(image, tuple(center[i]), tuple(axes[i]), angle[i], 0, 360, color, thickness=-1)
        
    return image

def main():
    # load images
    image_paths_train, label_paths_train = read_files("data/yolov5-class0/train")
    image_paths_valid, label_paths_valid = read_files("data/yolov5-class0/valid")
    image_paths = image_paths_train + image_paths_valid
    label_paths = label_paths_train + label_paths_valid

    for image_path, label_path in zip(image_paths, label_paths):
        image = cv2.imread(image_path)

        # calculate tree points
        points_tree1 = calc_tree_points((340, 0), 50.0, 90.0, 8)
        points_tree2 = calc_tree_points((340, 180), 50.0, 90.0, 8)
        points_tree = np.concatenate([points_tree1, points_tree2])
        # points: [[[start_x, start_y], [end_x, end_y]], [[start_x, start_y], [end_x, end_y]], ...]

        # draw tree
        big_image = cv2.resize(image, dsize=None, fx=2.0, fy=2.0)
        big_image = draw_lines(big_image, points_tree)
        big_image = draw_bubbles(big_image)
        image_addedObject = cv2.resize(big_image, dsize=None, fx=0.5, fy=0.5)

        # write training image
        cv2.imwrite(image_path.replace(".jpg", "_object.jpg"), image_addedObject)
        shutil.copyfile(label_path, label_path.replace(".txt", "_object.txt"))


if __name__ == "__main__":
    main()