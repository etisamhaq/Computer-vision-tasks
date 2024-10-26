import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = "image.png"  # Replace with your image path
img = cv2.imread(image_path)

# Convert BGR to RGB for displaying via matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Perform flipping
horizontal_flip = cv2.flip(img_rgb, 1)  # Horizontal flip
vertical_flip = cv2.flip(img_rgb, 0)    # Vertical flip
both_flip = cv2.flip(img_rgb, -1)       # Flip both axes

# Display the images using matplotlib
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

# Original image
axs[0].imshow(img_rgb)
axs[0].set_title("Original")
axs[0].axis('off')

# Horizontally flipped image
axs[1].imshow(horizontal_flip)
axs[1].set_title("Horizontal Flip")
axs[1].axis('off')

# Vertically flipped image
axs[2].imshow(vertical_flip)
axs[2].set_title("Vertical Flip")
axs[2].axis('off')

# Both flipped image
axs[3].imshow(both_flip)
axs[3].set_title("Both Flipped")
axs[3].axis('off')

plt.show()
