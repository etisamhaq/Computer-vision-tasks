import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'image1.png', cv2.IMREAD_COLOR)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Arithmetic operations
weightedSum = cv2.add(gray, 90)           # Add 90 to all pixel values
weightedSubtract = cv2.subtract(gray, 90) # Subtract 90 from all pixel values
weightedMultiply = cv2.multiply(gray, 1.5) # Multiply pixel values by 1.5
weightedDivide = cv2.divide(gray, 1.5)    # Divide pixel values by 1.5

# Logical operations
invert = cv2.bitwise_not(gray)  # Invert the grayscale image

# Create a mask for logical operations (a simple binary mask)
mask = np.zeros_like(gray)
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)  # White rectangle on a black background

bitwise_and = cv2.bitwise_and(gray, mask)  # AND operation with the mask
bitwise_or = cv2.bitwise_or(gray, mask)    # OR operation with the mask
bitwise_xor = cv2.bitwise_xor(gray, mask)  # XOR operation with the mask

# Display the images
fig = plt.figure(figsize=(10, 10))

# Original Image
fig.add_subplot(3, 3, 1)
plt.title('Original')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Show in RGB for correct color display
plt.axis('off')

# Grayscale Image
fig.add_subplot(3, 3, 2)
plt.title('Grayscale')
plt.imshow(gray, cmap='gray')
plt.axis('off')

# Addition
fig.add_subplot(3, 3, 3)
plt.title('Add 90')
plt.imshow(weightedSum, cmap='gray')
plt.axis('off')

# Subtraction
fig.add_subplot(3, 3, 4)
plt.title('Subtract 90')
plt.imshow(weightedSubtract, cmap='gray')
plt.axis('off')

# Multiplication
fig.add_subplot(3, 3, 5)
plt.title('Multiply by 1.5')
plt.imshow(weightedMultiply, cmap='gray')
plt.axis('off')

# Division
fig.add_subplot(3, 3, 6)
plt.title('Divide by 1.5')
plt.imshow(weightedDivide, cmap='gray')
plt.axis('off')

# Inversion
fig.add_subplot(3, 3, 7)
plt.title('Invert')
plt.imshow(invert, cmap='gray')
plt.axis('off')

# Bitwise AND
fig.add_subplot(3, 3, 8)
plt.title('Bitwise AND')
plt.imshow(bitwise_and, cmap='gray')
plt.axis('off')

# Bitwise OR
fig.add_subplot(3, 3, 9)
plt.title('Bitwise OR')
plt.imshow(bitwise_or, cmap='gray')
plt.axis('off')

# Show the plot
plt.tight_layout()
plt.show()

# For XOR, we display separately because of space
fig2 = plt.figure(figsize=(4, 4))
plt.title('Bitwise XOR')
plt.imshow(bitwise_xor, cmap='gray')
plt.axis('off')
plt.show()
