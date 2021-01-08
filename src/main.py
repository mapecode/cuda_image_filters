import sys
import cv2
import numpy as np
import PIL.Image
from argparse import ArgumentParser
from filters import gaussian
from utils import create_gaussian_kernel
from constants import KERNEL_FILE, RESULT_FILE


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('image_src', help='source image file path')
    filter_group = parser.add_mutually_exclusive_group(required=True)

    filter_group.add_argument(
        '--gaussian',
        help='gaussian blur filter',
        action='store_true'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.gaussian:
        try:
            img_array = np.array(PIL.Image.open(args.image_src))
            kernel = np.load(KERNEL_FILE)
        except FileNotFoundError as e:
            print('File Not Found')
            sys.exit(e)

        result_img_array = gaussian.apply(img_array, kernel)

        PIL.Image.fromarray(result_img_array).save(RESULT_FILE)
