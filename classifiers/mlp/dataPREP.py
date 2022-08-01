"""
Global Feature Descriptors
These are the feature descriptors that quantifies an image globally. These don’t have the concept of interest points and thus, takes in the entire image for processing. Some of the commonly used global feature descriptors are

Color - Color Channel Statistics (Mean, Standard Deviation) and Color Histogram
Shape - Hu Moments, Zernike Moments
Texture - Haralick Texture, Local Binary Patterns (LBP)
Others - Histogram of Oriented Gradients (HOG), Threshold Adjancency Statistics (TAS)
"""
"""
Local Feature Descriptors
These are the feature descriptors that quantifies local regions of an image. Interest points are determined in the entire image and image patches/regions surrounding those interest points are considered for analysis. Some of the commonly used local feature descriptors are

SIFT (Scale Invariant Feature Transform)
SURF (Speeded Up Robust Features)
ORB (Oriented Fast and Rotated BRIEF)
BRIEF (Binary Robust Independed Elementary Features)
"""

import numpy as np
import random
import os
import cv2
import pickle
import matplotlib.pyplot as plt
import glob


#127 to 210 not rotate
categories = ["NORMAL","STEGGED"]

lsb = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\lcb\\all"
dct ="C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\dct\\all"
lsbran ="C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\lcbran\\all"

lsb_output = "C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\new-set-completly-internet\\lsb\\small_set"
lsbran_output = "C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\new-set-completly-internet\\lsbRan\\small_set" 
dct_output = "C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\new-set-completly-internet\\dct\\small_set"

dirs = [lsb,lsbran,dct]
dirs_output = [lsb_output,lsbran_output,dct_output]

main_path = dirs[2]
created_path = dirs_output[2]




train_path = os.path.join(main_path,"train")
test_path = os.path.join(main_path,"test")
validation_path = os.path.join(main_path,"valid")

histo_train = os.path.join(created_path,"small_set_histogram_train.pickle")
histro_test = os.path.join(created_path,"small_set_histogram_test.pickle")
histro_valid = os.path.join(created_path,"small_set_histogram_valid.pickle")


all_path = [train_path,test_path,validation_path]
file_to_pickle = [histo_train,histro_test,histro_valid]

bins = 8


def extract_historgram(image, mask=None):
    #convert the image to HSV color-space
    image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #compute the color historgram
    hist = cv2.calcHist([image], [0,1,2], None, [bins,bins,bins], [0, 256, 0, 256, 0, 256])
    #normalize the histogram
    cv2.normalize(hist,hist)
    return hist.flatten()






for one_path in all_path:

    data = [] # features and its labels will be stored in this (historgram)

    file_index = all_path.index(one_path)

    for category in categories:
        path = os.path.join(one_path,category)
        label = categories.index(category)
        print(label,' ',categories[label],' ',one_path)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            item_img = cv2.imread(img_path)
            item_img = cv2.resize(item_img,(500,500))
            ####################################
            # Global Feature extraction
            ####################################
            historgram_feature = extract_historgram(item_img)
            data.append([historgram_feature,label])

    random.shuffle(data)
    print("[STATUS]! "+file_to_pickle[file_index]," file creating!")
    pickle_write = open(file_to_pickle[file_index],'wb')
    pickle.dump(data,pickle_write)
    print("[UPDATE]! "+file_to_pickle[file_index]," file created!")
    pickle_write.close()

