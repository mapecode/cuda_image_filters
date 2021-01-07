import numpy as np
import PIL.Image
from argparse import ArgumentParser
from filters import blur
from utils import create_gaussian_kernel


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('image_src', help='source image file path')
    filter_group = parser.add_mutually_exclusive_group(required=True)

    filter_group.add_argument(
        '-g',
        help='grayscale filter',
        action='store_true'
    )
    filter_group.add_argument(
        '-b',
        help='blur filter',
        action='store_true'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if(args.b):
        try:
            img_array = np.array(PIL.Image.open(args.image_src))
        except FileNotFoundError as e:
            print('File Not Found')
            sys.exit(e)

        kernel = create_gaussian_kernel()
        result_img_array = blur.apply_blur(img_array, kernel)

        PIL.Image.fromarray(result_img_array).save('result.png')
