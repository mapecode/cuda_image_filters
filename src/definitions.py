import pycuda.driver as drv


drv.init()
device = drv.Device(0)

# RGB
RED = 0
GREEN = 1
BLUE = 2

# Files
KERNEL_FILE = './exec/kernel.npy'
RESULT_FILE = 'result.png'
CUDA_GAUSSIAN = './cuda/gaussian.cu'
CUDA_GAUSSIAN_FUNCTION = 'apply_gaussian'
CUDA_GRAYSCALE = './cuda/grayscale.cu'
CUDA_GRAYSCALE_FUNCTION = 'apply_grayscale'
CUDA_BLUE = './cuda/blue.cu'
CUDA_BLUE_FUNCTION = 'apply_blue'

# Cuda
DIM_BLOCK = 32
MAX_GRID_DIM_X = device.MAX_GRID_DIM_X
MAX_GRID_DIM_Y = device.MAX_GRID_DIM_Y
MAX_NUM_BLOCKS = device.MAX_GRID_DIM_X * device.MAX_GRID_DIM_Y

# Gaussian Kernel
STANDARD_DEVIATION = 3.99
FILTER_WIDTH = 3 * int(STANDARD_DEVIATION)
