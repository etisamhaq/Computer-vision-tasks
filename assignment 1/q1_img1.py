import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_image_1(outer_size, inner_size):
    fig, ax = plt.subplots(figsize=(5, 5))

    outer_square = patches.Rectangle((0, 0), outer_size, outer_size, color='black')
    ax.add_patch(outer_square)
    

    offset = (outer_size - inner_size) / 2

    inner_square = patches.Rectangle((offset, offset), inner_size, inner_size, color='white')
    ax.add_patch(inner_square)
    

    ax.set_xlim(0, outer_size)
    ax.set_ylim(0, outer_size)
    ax.axis('off')
    plt.show()

draw_image_1(outer_size=10, inner_size=4)
