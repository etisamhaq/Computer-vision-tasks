import numpy as np
import matplotlib.pyplot as plt

def create_colored_corners(image_size):
    if image_size < 10:
        print("Image size too small! Please choose a size greater than or equal to 10.")
        return
    
    image = np.ones((image_size, image_size, 3))
    
    box_size = image_size // 10
    
    colors = {
        "black": [0, 0, 0],   # Black box
        "blue": [0, 0, 1],    # Blue box
        "green": [0, 1, 0],   # Green box
        "red": [1, 0, 0]      # Red box
    }
    
    image[:box_size, :box_size] = colors['black']
    
    image[:box_size, -box_size:] = colors['blue']
    
    image[-box_size:, :box_size] = colors['green']
    
    image[-box_size:, -box_size:] = colors['red']
    
    plt.imshow(image)
    plt.axis('off')  # Hide the axes
    plt.show()

create_colored_corners(image_size=100)
