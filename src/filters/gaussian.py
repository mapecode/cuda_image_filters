import numpy as np
import math
import pycuda.autoinit
from pycuda import driver
from pycuda.compiler import SourceModule
from constants import *

apply_filter = SourceModule(
    open(CUDA_GAUSSIAN).read()).get_function(CUDA_GAUSSIAN_FUNCTION)


def apply(img_array, kernel):
    if len(img_array.shape) != 3:
        raise ValueError('Error, the image must be in RGB')

    rgb_channels = [
        img_array[:, :, 0].copy(),
        img_array[:, :, 1].copy(),
        img_array[:, :, 2].copy(),
    ]

    height, width = img_array.shape[:2]

    dim_grid_x = math.ceil(width / DIM_BLOCK)
    dim_grid_y = math.ceil(height / DIM_BLOCK)

    if (dim_grid_x * dim_grid_y) > MAX_NUM_BLOCKS:
        raise ValueError(
            'Error, maximum block number exceeded')
    else:

        for channel in rgb_channels:
            apply_filter(
                driver.In(channel),
                driver.Out(channel),
                np.uint32(width),
                np.uint32(height),
                driver.In(kernel),
                np.uint32(len(kernel)),
                block=(DIM_BLOCK, DIM_BLOCK, 1),
                grid=(dim_grid_x, dim_grid_y),
            )

        result_img_array = np.empty_like(img_array)

        result_img_array[:, :, 0] = rgb_channels[0]
        result_img_array[:, :, 1] = rgb_channels[1]
        result_img_array[:, :, 2] = rgb_channels[2]

        return result_img_array
