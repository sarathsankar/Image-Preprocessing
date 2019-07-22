#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Author: Sarath KS
Date: 21/07/2019
E-mail: sarathks333@gmail.com
'''
# Dependencies
import sys
import cv2
import glob
from os.path import join, split


class Color2Gray(object):
    '''
    source_dir_path: Directory path to source images(No nested directory in target directory).
    target_dir_path: Path to target directory to write results.
    img_type: Image type. eg: png(=default), jpeg

    # Command line usage
    $ python3 color2gray.py <source_dir_path> <target_dir_path> 
    '''
    def __init__(self, source_dir_path=None, target_dir_path=None, img_type='png', img_shape=(128, 128)):
        self.source_dir_path = source_dir_path
        self.target_dir_path = target_dir_path
        self.img_type = img_type
        self.img_shape = list(map(int, img_shape.split(','))) if type(img_shape) == str else img_shape

    def run(self):
        c = 0
        for fpath in glob.glob(join(self.source_dir_path, '*.'+self.img_type)):
            name = split(fpath)[-1]
            image = cv2.imread(fpath)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image_gray = cv2.resize(image_gray, self.img_shape)
            cv2.imwrite(join(self.target_dir_path, name), image_gray)
            c += 1
        print("Total images processed: {}".format(c))

            
if __name__ == "__main__":
    print("Calling Color2Gray...")
    args = {'source_dir_path': sys.argv[1],
            'target_dir_path': sys.argv[2]}
    obj = Color2Gray(**args)
    try:
        obj.run()
        print("Success....!!!")
    except Exception as e:
        print("Exception: ", e)