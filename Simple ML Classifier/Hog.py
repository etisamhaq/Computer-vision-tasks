import numpy as np


cell = [8, 8]

incr = [8,8]
#total bins
#hence feature Descriptor is (9*4) 36*7*15= 3780
bin_num = 9

# image height and width
max_h = 128
max_w = 64


def create_grad_array(image):
    
	# local contrast normalisation
    
    image = (image-np.mean(image))/np.std(image)

 #   max_h = 128
  #  max_w = 64

    grad = np.zeros((max_h, max_w))
    mag = np.zeros((max_h, max_w))
	
    for h,row in enumerate(image):
        for w, val in enumerate(row):		
             if h-1>=0 and w-1>=0 and h+1<max_h and w+1<max_w:
                dy= image[h+1][w]-image[h-1][w] #change in dx, Change in dy or apply sobel operators
                dx = row[w+1]-row[w-1]+0.0001 #avoid divide by zero
                grad[h][w] = np.arctan(dy/dx)*(180/np.pi)   #tan(Φ) = dy / dx or Φ = atan(dy / dx)
                if grad[h][w]<0:
                    grad[h][w] += 180
                mag[h][w] = np.sqrt(dx*dx+dy*dy)   #Total Gradient Magnitude =  √[(dx)2+(dy)2]

    return grad,mag

def create_hog_features(grad_array,mag_array):

	max_h = int(((grad_array.shape[0]-cell[0])/incr[0])+1)
	max_w = int(((grad_array.shape[1]-cell[1])/incr[1])+1)
	cell_array = []
	w = 0
	h = 0
	i = 0
	j = 0

	#Creating 8X8 cells
	while i<max_h:
		w = 0
		j = 0

		while j<max_w:
			for_hist = grad_array[h:h+cell[0],w:w+cell[1]]
			for_wght = mag_array[h:h+cell[0],w:w+cell[1]]
			
			val = calculate_histogram(for_hist,for_wght)
			cell_array.append(val)
			j += 1
			w += incr[1]

		i += 1
		h += incr[0]

	cell_array = np.reshape(cell_array,(max_h, max_w, bin_num))
	#normalising blocks of cells
	block = [2,2]
	#here increment is 1

	max_h = int((max_h-block[0])+1)
	max_w = int((max_w-block[1])+1)
	block_list = []
	w = 0
	h = 0
	i = 0
	j = 0

	while i<max_h:
		w = 0
		j = 0

		while j<max_w:
			for_norm = cell_array[h:h+block[0],w:w+block[1]]
			mag = np.linalg.norm(for_norm)
			arr_list = (for_norm/mag).flatten().tolist()
			block_list += arr_list
			j += 1
			w += 1

		i += 1
		h += 1

	#returns list of 3780 elements
	return block_list

def calculate_histogram(array,weights):
	bins_range = (0, 180)
	bins = bin_num
	hist,_ = np.histogram(array,bins=bins,range=bins_range,weights=weights)

	return hist

def hog1(gray, pixels_per_cell, cells_per_block): # fd= feature descriptor

    gradient,magnitude = create_grad_array(gray)
    hog_features = create_hog_features(gradient,magnitude)
    hog_features = np.asarray(hog_features,dtype=float)
	

    return hog_features