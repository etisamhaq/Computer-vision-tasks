import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_image_2(image_size, box_size):
    fig, ax = plt.subplots(figsize=(5, 5))
    

    positions = [(0, 0), (0, image_size - box_size), (image_size - box_size, 0), (image_size - box_size, image_size - box_size)]
    
    for pos in positions:
        square = patches.Rectangle(pos, box_size, box_size, color='black')
        ax.add_patch(square)
    
    ax.set_xlim(0, image_size)
    ax.set_ylim(0, image_size)
    ax.axis('off')
    plt.show()

draw_image_2(image_size=10, box_size=1)
