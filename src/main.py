import sys
import timeit
import numpy as np
import PIL.Image
from argparse import ArgumentParser
from definitions import RESULT_FILE


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('image_src', help='source image file path')
    filter_group = parser.add_mutually_exclusive_group(required=True)

    filter_group.add_argument(
        '--gaussian',
        help='gaussian blur filter',
        action='store_true'
    )
    filter_group.add_argument(
        '--grayscale',
        help='grayscale filter',
        action='store_true'
    )
    filter_group.add_argument(
        '--blue',
        help='grayscale filter',
        action='store_true'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.gaussian:
        from filters import gaussian
        from definitions import KERNEL_FILE

        try:
            img_array = np.array(PIL.Image.open(args.image_src))
            kernel = np.load(KERNEL_FILE)
        except FileNotFoundError as e:
            print('File Not Found')
            sys.exit(e)

        start_time = timeit.default_timer()
        result_img_array = gaussian.apply(img_array, kernel)

        print('Time apply gaussian filter:',
              timeit.default_timer() - start_time, "s")

        PIL.Image.fromarray(result_img_array).save(RESULT_FILE)
    elif args.grayscale:
        from filters import grayscale

        try:
            img_array = np.array(PIL.Image.open(args.image_src))
        except FileNotFoundError as e:
            print('File Not Found')
            sys.exit(e)

        start_time = timeit.default_timer()
        result_img_array = grayscale.apply(img_array)

        print('Time apply grayscale filter:',
              timeit.default_timer() - start_time, "s")

        PIL.Image.fromarray(result_img_array).save(RESULT_FILE)
    elif args.blue:
        from filters import blue

        try:
            img_array = np.array(PIL.Image.open(args.image_src))
        except FileNotFoundError as e:
            print('File Not Found')
            sys.exit(e)

        start_time = timeit.default_timer()
        result_img_array = blue.apply(img_array)

        print('Time apply blue filter:',
              timeit.default_timer() - start_time, "s")

        PIL.Image.fromarray(result_img_array).save(RESULT_FILE)
