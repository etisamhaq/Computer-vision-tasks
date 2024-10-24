import numpy as np
import matplotlib.pyplot as plt

def nearest_neighbor_resize(image, new_width, new_height):
    original_height, original_width = image.shape
    resized_image = np.zeros((new_height, new_width), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            original_x = int(j * original_width / new_width)
            original_y = int(i * original_height / new_height)
            resized_image[i, j] = image[original_y, original_x]

    return resized_image

input_image = np.array([[1, 2], [3, 4]])  
resized_image_nn = nearest_neighbor_resize(input_image, 4, 4)

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(input_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Resized Image (Nearest Neighbor)")
plt.imshow(resized_image_nn, cmap='gray')

plt.show()
