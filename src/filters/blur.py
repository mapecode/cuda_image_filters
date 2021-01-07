import numpy as np
import math
import pycuda.autoinit
from pycuda import driver
from pycuda.compiler import SourceModule

DIM_BLOCK = 32
MAX_GRID_DIM_X = driver.device_attribute.MAX_GRID_DIM_X
MAX_GRID_DIM_Y = driver.device_attribute.MAX_GRID_DIM_Y
MAX_NUM_BLOCKS = pycuda.autoinit.device.get_attribute(
    MAX_GRID_DIM_X) * pycuda.autoinit.device.get_attribute(MAX_GRID_DIM_Y)

RED = 0
GREEN = 1
BLUE = 2

CUDA_APPLY_KERNEL = 'cuda/apply_kernel.cu'


def apply_blur(img_array, kernel):
    result_img_array = np.empty_like(img_array)

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
            'image dimensions too great, maximum block number exceeded')
    else:
        apply_filter = SourceModule(
            open(CUDA_APPLY_KERNEL).read()).get_function('apply_kernel')

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

        result_img_array[:, :, RED] = rgb_channels[RED]
        result_img_array[:, :, GREEN] = rgb_channels[GREEN]
        result_img_array[:, :, BLUE] = rgb_channels[BLUE]

        return result_img_array
