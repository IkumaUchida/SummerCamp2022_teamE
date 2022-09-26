import os
import sys
import glob

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
        image_cp = cv2.line(image_cp, pair_start, pair_end, (19, 93, 30), thickness=1, lineType=cv2.LINE_AA)
    return image_cp

def main():
    # load images
    image_paths, _ = read_files()
    images = []
    for path in image_paths:
        images.append(cv2.imread(path))

    # calculate tree points
    points = calc_tree_points((400, 20), 50.0, 90.0, 8)
    # points: [[[start_x, start_y], [end_x, end_y]], [[start_x, start_y], [end_x, end_y]], ...]

    # draw tree
    big_image = cv2.resize(images[0], dsize=None, fx=2.0, fy=2.0)
    big_image = draw_lines(big_image, points)
    image = cv2.resize(big_image, dsize=None, fx=0.5, fy=0.5)

    # write image
    cv2.imwrite(image_paths[0].replace(".jpg", "_tree.jpg"), image)
    
    # For sample image
    cv2.imwrite("/workspace/scripts/data_augmentation/sample/original.jpg", images[0])
    cv2.imwrite("/workspace/scripts/data_augmentation/sample/add_tree.jpg", image)


if __name__ == "__main__":
    main()