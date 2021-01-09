__global__ void apply_blue(unsigned char *red_channel,unsigned char *green_channel, 
    const unsigned int width, const unsigned int height) {
    const unsigned int row = threadIdx.y + blockIdx.y * blockDim.y;
    const unsigned int col = threadIdx.x + blockIdx.x * blockDim.x;

    if(row < height && col < width) {
        int index = col + row * width;
        red_channel[index] = green_channel[index] = 0;
    }
}
