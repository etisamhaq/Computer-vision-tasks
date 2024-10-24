import matplotlib.pyplot as plt

def draw_image_3(image_size, line_size, num_lines):
    fig, ax = plt.subplots(figsize=(5, 5))
    
    spacing = image_size / (num_lines + 1)
    
    # Draw horizontal lines
    for i in range(1, num_lines + 1):
        ax.plot([0, image_size], [i * spacing, i * spacing], color='black', lw=line_size)
    
    # Draw vertical lines
    for i in range(1, num_lines + 1):
        ax.plot([i * spacing, i * spacing], [0, image_size], color='black', lw=line_size)
    
    ax.set_xlim(0, image_size)
    ax.set_ylim(0, image_size)
    ax.axis('off')
    plt.show()

draw_image_3(image_size=10, line_size=1, num_lines=5)
