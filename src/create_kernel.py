from numpy import save
from argparse import ArgumentParser

from utils import create_gaussian_kernel


def parse_args():
    parser = ArgumentParser()

    filter_group = parser.add_mutually_exclusive_group(required=True)

    filter_group.add_argument(
        '--gaussian',
        help='gaussian kernel for blur filter',
        action='store_true'
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.gaussian:
        kernel = create_gaussian_kernel()
        save('./exec/kernel.npy', kernel)
