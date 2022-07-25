import numpy as np
import random
import os
import cv2
import pickle
from progress.bar import PixelBar
import matplotlib.pyplot as plt



internet_data_set = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-SET\\small-set\\DCT\\all"

categories = ["NORMAL","STEGGED"]

save_path = "C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\NEW-set\\dct_dataset"

histogram_path = os.path.join(save_path,"small_set_small.pickle")
bins = 8




def extract_historgram(image, mask=None):
    #convert the image to HSV color-space
    image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #compute the color historgram
    hist = cv2.calcHist([image], [0,1,2], None, [bins,bins,bins], [0, 256, 0, 256, 0, 256])
    #normalize the histogram
    cv2.normalize(hist,hist)
    return hist.flatten()


data = [] # features and its labels will be stored in this (historgram)
pixelBar = PixelBar('Image Stagging',max=len(categories))
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
        data.append([historgram_feature,label])

pixelBar.finish()
random.shuffle(data)

pickle_write = open(histogram_path,'wb')
pickle.dump(data,pickle_write)
print(histogram_path," file created!")
pickle_write.close()
