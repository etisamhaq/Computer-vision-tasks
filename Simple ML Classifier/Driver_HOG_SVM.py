from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report,ConfusionMatrixDisplay,confusion_matrix


from sklearn.model_selection import train_test_split

import numpy as np

#import cv2
import os

from PIL import Image # This will be used to read/modify images (can be done via OpenCV too)
from numpy import *
from Hog import hog1

# define parameters of HOG feature extraction

pixels_per_cell = (8, 8)
cells_per_block = (2, 2)



# define path to images:

pos_im_path = r"trainImages\positive" # This is the path of our positive input dataset
# define the same for negatives
neg_im_path= r"trainImages\negative"

# read the image files:
pos_im_listing = os.listdir(pos_im_path) # it will read all the files in the positive image path (so all the required images)
neg_im_listing = os.listdir(neg_im_path)
num_pos_samples = size(pos_im_listing) # simply states the total no. of images
num_neg_samples = size(neg_im_listing)
print("Count of Positive Samples: ",num_pos_samples) 
print("Count of Negative Samples: ",num_neg_samples)


data= []
labels = []
#fd=np.zeros(())

# compute HOG features and label them:

i=0
##########3# Pre-Process Negative images
for file in pos_im_listing: #this loop enables reading the files in the pos_im_listing variable one by one
    img = Image.open(pos_im_path + '\\' + file) # open the file
    img = img.resize((64,128))
    gray = img.convert('L') # convert the image into single channel i.e. RGB to grayscale
    # calculate HOG for positive features
    fd = hog1(gray, pixels_per_cell, cells_per_block)# fd= feature descriptor
   
    #print(len(fd))
    #f=np.asarray(fd)
    #print(fd.shape)
    data.append(fd)
    labels.append(1)
    
############## Pre-Process Negative images
for file in neg_im_listing:
    img= Image.open(neg_im_path + '\\' + file)
    img = img.resize((64,128))
    gray= img.convert('L')
    # Now we calculate the HOG for negative features
    fd = hog1(gray, pixels_per_cell, cells_per_block) 
   

    #print(len(fd))
    #f=np.asarray(fd)
    #print(fd.shape)
    data.append(fd)
    labels.append(0)
    
    
    
# encode the labels, converting them from strings to integers
le = LabelEncoder()
labels = le.fit_transform(labels)

print(len(labels))
print(len(data))

##############
# Split data Train 80% Test 20%

print(" Constructing training/testing split...")
d=np.asarray(data,dtype=object)
(trainData, testData, trainLabels, testLabels) = train_test_split(
	data, labels, test_size=0.30, random_state=42)
print("Train Data: ",len(trainData))
print("Test Data: ",len(testData))
print("Train Labels: ",len(trainLabels))
print("Test Labels: ",len(testLabels))

########## Train the linear SVM
print(" Training Linear SVM classifier...")
model = LinearSVC()
model.fit(trainData, trainLabels)
##########Test the classifier
print(" Testing classifier on test data ...")
predictions = model.predict(testData)
print("Classification Report")
#label_name=[0,1]
print(classification_report(testLabels, predictions))
cm = confusion_matrix(testLabels, predictions, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot() 
