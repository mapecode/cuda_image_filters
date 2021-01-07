import numpy as np

STANDARD_DEVIATION = 7
FILTER_WIDTH = 3 * int(STANDARD_DEVIATION)


def create_gaussian_kernel():
    matrix = np.empty((FILTER_WIDTH, FILTER_WIDTH), np.float32)
    filter_half = FILTER_WIDTH // 2
    for i in range(-filter_half, filter_half + 1):
        for j in range(-filter_half, filter_half + 1):
            matrix[i + filter_half][j + filter_half] = (
                np.exp(-(i**2 + j**2) / (2 * STANDARD_DEVIATION**2))
                / (2 * np.pi * STANDARD_DEVIATION**2)
            )

    return matrix / matrix.sum()
