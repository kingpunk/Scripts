import numpy as np
import random
import os
import cv2
import pickle
import mahotas
from progress.bar import PixelBar
import matplotlib.pyplot as plt



internet_data_set = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\GLOBAL_TEST_SET\\capturedSet\\mid\\LSBRan\\test2"

categories = ["NORMAL","STEGGED"]

save_path = "C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\HISTOGRAM_FEATURE_EXTRACTION\\Comptuerd_set\\mid\\lsbran"

histogram_path = os.path.join(save_path,"global_mid_set_test2.pickle")
bins = 8




def extract_historgram(image, mask=None):
    #convert the image to HSV color-space
    image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #compute the color historgram
    hist = cv2.calcHist([image], [0,1,2], None, [bins,bins,bins], [0, 256, 0, 256, 0, 256])
    #normalize the histogram
    cv2.normalize(hist,hist)
    return hist.flatten()

"""

# HI Moments features extraction - Quantifies the shape of the images
def hu_moments_extraction(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature


# Haralick Texture - quantifies texture of the image

def haralick_feature_extraction(image):
    #convert the image to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #compute the haralick texture feature vector
    haralick_features = mahotas.features.haralick(gray).mean(axis=0)
    # return the results
    return haralick_features

"""




data = [] # features and its labels will be stored in this (historgram)
pixelBar = PixelBar('GLobal Feature extraction',max=len(categories))
for category in categories:
    path = os.path.join(internet_data_set,category)
    label = categories.index(category)
    pixelBar.next()
    print(' ',label,' ',categories[label],' ',path)

    for img in os.listdir(path):
        img_path = os.path.join(path,img)
        item_img = cv2.imread(img_path)
        item_img = cv2.resize(item_img,(500,500))
        ####################################
        # Global Feature extraction
        ####################################
        historgram_feature = extract_historgram(item_img)
       # harlick_feature = haralick_feature_extraction(item_img)
       # hu_movements = hu_moments_extraction(item_img)
        ####################################
        #Concatenate global features
        ####################################
        #global_features = np.hstack([historgram_feature,harlick_feature,hu_movements])
        data.append([historgram_feature,label])

pixelBar.finish()
random.shuffle(data)

pickle_write = open(histogram_path,'wb')
pickle.dump(data,pickle_write)
print(histogram_path," file created!")
pickle_write.close()
