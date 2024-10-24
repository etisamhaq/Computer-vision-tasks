from PIL import Image
import numpy as np

def mirror_image_grayscale(image_path, output_path):

    image = Image.open(image_path).convert("L") 
    
    image_array = np.array(image)
    
    height, width = image_array.shape
    
    if height % 2 != 0:
        image_array = image_array[:-1, :]
        height -= 1
    
    upper_half = image_array[:height//2, :]
    lower_half = image_array[height//2:, :]
    
    mirrored_lower_half = np.flipud(lower_half)
    image_array[:height//2, :] = mirrored_lower_half
    
    mirrored_image = Image.fromarray(image_array)
    
    mirrored_image.save(output_path)

    print(f"Mirrored image saved to {output_path}")

mirror_image_grayscale('park.jpg', 'output.jpg')
