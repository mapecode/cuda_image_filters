import numpy as np
from definitions import KERNEL_FILE, STANDARD_DEVIATION, FILTER_WIDTH


def create_gaussian_kernel():
    matrix = np.empty((FILTER_WIDTH, FILTER_WIDTH), np.float32)
    filter_half = FILTER_WIDTH // 2

    for i in range(-filter_half, filter_half+1):
        for j in range(-filter_half, filter_half+1):
            matrix[i+filter_half, j + filter_half] = (1/2*np.pi*(
                STANDARD_DEVIATION**2))*np.exp(-(i**2 + j**2)/(2 * STANDARD_DEVIATION**2))

    return matrix / matrix.sum()


if __name__ == "__main__":
    kernel = create_gaussian_kernel()
    np.save(KERNEL_FILE, kernel)
