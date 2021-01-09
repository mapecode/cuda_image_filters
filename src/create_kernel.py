from numpy import save
from argparse import ArgumentParser

from utils import *
from definitions import KERNEL_FILE

if __name__ == "__main__":
    kernel = create_gaussian_kernel()
    save(KERNEL_FILE, kernel)
