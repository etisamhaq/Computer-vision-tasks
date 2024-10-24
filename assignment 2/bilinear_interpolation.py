from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def bilinear_resize(image, new_width, new_height):
    original_height, original_width = image.shape
    resized_image = np.zeros((new_height, new_width), dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):
            x = j * original_width / new_width
            y = i * original_height / new_height
            
            x0 = int(x)
            x1 = min(x0 + 1, original_width - 1)
            y0 = int(y)
            y1 = min(y0 + 1, original_height - 1)

            a = x - x0
            b = y - y0

            top = (1 - a) * image[y0, x0] + a * image[y0, x1]
            bottom = (1 - a) * image[y1, x0] + a * image[y1, x1]
            resized_image[i, j] = (1 - b) * top + b * bottom

    return resized_image

def read_png(image_path):
    image = Image.open(image_path).convert('L')  
    return np.array(image)


image_path = 'image.png'  
input_image = read_png(image_path)

new_width = 200  # Specify the new width
new_height = 200  # Specify the new height
resized_image_bilinear = bilinear_resize(input_image, new_width, new_height)


plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(input_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Resized Image (Bilinear)")
plt.imshow(resized_image_bilinear, cmap='gray')

plt.show()
