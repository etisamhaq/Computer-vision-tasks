import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = "image.png"  # Replace with your image path
img = cv2.imread(image_path)

# Convert BGR to RGB for displaying via matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Perform rotations
rotate_90_clockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)  # 90 degrees clockwise
rotate_180 = cv2.rotate(img_rgb, cv2.ROTATE_180)                    # 180 degrees
rotate_90_counterclockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 270 degrees (90 degrees counterclockwise)

# Display the images using matplotlib
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

# Original image
axs[0].imshow(img_rgb)
axs[0].set_title("Original")
axs[0].axis('off')

# 90 degrees clockwise
axs[1].imshow(rotate_90_clockwise)
axs[1].set_title("90° Clockwise")
axs[1].axis('off')

# 180 degrees rotation
axs[2].imshow(rotate_180)
axs[2].set_title("180° Rotation")
axs[2].axis('off')

# 270 degrees clockwise (90 degrees counterclockwise)
axs[3].imshow(rotate_90_counterclockwise)
axs[3].set_title("270° Clockwise")
axs[3].axis('off')

plt.show()
