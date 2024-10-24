from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(size, sigma=1):
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * 
                     np.exp(-((x - (size - 1) / 2)**2 + (y - (size - 1) / 2)**2) / (2 * sigma**2)),
        (size, size)
    )
    return kernel / np.sum(kernel)

def convolve(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')
    convolved_image = np.zeros(image.shape)

    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + kernel_height, j:j + kernel_width]
            convolved_image[i, j] = np.sum(region * kernel)

    return convolved_image

def read_png(image_path):
    image = Image.open(image_path).convert('L')
    return np.array(image)

def apply_gaussian_filter(image, kernel_size=3, sigma=1):
    kernel = gaussian_kernel(kernel_size, sigma)
    return convolve(image, kernel)

image_path = 'image.png'
input_image = read_png(image_path)

filtered_image = apply_gaussian_filter(input_image, kernel_size=3, sigma=1)

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(input_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Filtered Image (Gaussian)")
plt.imshow(filtered_image, cmap='gray')

plt.show()
