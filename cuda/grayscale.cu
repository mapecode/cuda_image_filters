#define RED_MULTIPLIER 0.2986
#define GREEN_MULTIPLIER 0.587
#define BLUE_MULTIPLIER 0.114

__global__ void apply_grayscale(unsigned char *red_channel,unsigned char *green_channel,
    unsigned char *blue_channel, const unsigned int width, const unsigned int height) {
    const unsigned int row = threadIdx.y + blockIdx.y * blockDim.y;
    const unsigned int col = threadIdx.x + blockIdx.x * blockDim.x;

    if(row < height && col < width) {
        int index = col + row * width;
        unsigned char intensity = static_cast<unsigned char>(
            red_channel[index] * RED_MULTIPLIER + green_channel[index] * GREEN_MULTIPLIER + blue_channel[index] * BLUE_MULTIPLIER
        );

        red_channel[index] = green_channel[index] = blue_channel[index] = 
            intensity < 255 ? intensity : 255;
    }
}
