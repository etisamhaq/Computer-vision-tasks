import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "image.png"  # Replace with your image path
img = cv2.imread(image_path)

# Convert BGR to RGB for displaying via matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get the dimensions of the original image
height, width, _ = img_rgb.shape

# Flip the images
horizontal_flip = cv2.flip(img_rgb, 1)  # Horizontal flip
vertical_flip = cv2.flip(img_rgb, 0)    # Vertical flip
both_flip = cv2.flip(img_rgb, -1)       # Both axis flip

# Rotate the images
rotate_90_clockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)      # 90 degrees clockwise
rotate_180 = cv2.rotate(img_rgb, cv2.ROTATE_180)                        # 180 degrees
rotate_90_counterclockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 270 degrees (90 counterclockwise)

# Resize rotated images to match original dimensions
rotate_90_clockwise_resized = cv2.resize(rotate_90_clockwise, (width, height))
rotate_180_resized = cv2.resize(rotate_180, (width, height))
rotate_90_counterclockwise_resized = cv2.resize(rotate_90_counterclockwise, (width, height))

# i) Concatenate the original and flipped images horizontally
concatenated_flips = cv2.hconcat([img_rgb, horizontal_flip, vertical_flip, both_flip])

# ii) Concatenate all the rotated images horizontally
concatenated_rotations = cv2.hconcat([rotate_90_clockwise_resized, rotate_180_resized, rotate_90_counterclockwise_resized])

# Display the concatenated images
fig, axs = plt.subplots(2, 1, figsize=(15, 10))

# Show concatenated flipped images
axs[0].imshow(concatenated_flips)
axs[0].set_title("Original and Flipped Images Concatenated")
axs[0].axis('off')

# Show concatenated rotated images
axs[1].imshow(concatenated_rotations)
axs[1].set_title("Rotated Images Concatenated")
axs[1].axis('off')

plt.show()
