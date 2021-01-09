import numpy as np
import math
import pycuda.autoinit
from pycuda import driver
from pycuda.compiler import SourceModule
from definitions import *

apply_grayscale_filter = SourceModule(
    open(CUDA_GRAYSCALE).read()).get_function(CUDA_GRAYSCALE_FUNCTION)


def apply(img_array):
    if len(img_array.shape) != 3:
        raise ValueError('Error, the image must be in RGB')

    rgb_channels = [
        img_array[:, :, RED].copy(),
        img_array[:, :, GREEN].copy(),
        img_array[:, :, BLUE].copy(),
    ]

    height, width = img_array.shape[:2]

    dim_grid_x = math.ceil(width / DIM_BLOCK)
    dim_grid_y = math.ceil(height / DIM_BLOCK)

    if (dim_grid_x * dim_grid_y) > MAX_NUM_BLOCKS:
        raise ValueError(
            'Error, maximum block number exceeded')
    else:
        apply_grayscale_filter(
            driver.InOut(rgb_channels[RED]),
            driver.InOut(rgb_channels[GREEN]),
            driver.InOut(rgb_channels[BLUE]),
            np.uint32(width),
            np.uint32(height),
            block=(DIM_BLOCK, DIM_BLOCK, 1),
            grid=(dim_grid_x, dim_grid_y)
        )

        result_img_array = np.empty_like(img_array)

        result_img_array[:, :, RED] = rgb_channels[RED]
        result_img_array[:, :, GREEN] = rgb_channels[GREEN]
        result_img_array[:, :, BLUE] = rgb_channels[BLUE]

        return result_img_array
