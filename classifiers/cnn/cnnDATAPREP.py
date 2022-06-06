"""
[x]create a pikle data of the main data (large data set) 
[x]After this create a different folder with a mix of all the file (stegged and normal)
and with code create 80%-10%-10% split where 
80 - training data (936 -total 468 each)
10 - testing data (117 - total 59 - 58 split)
10 - validating data (117 - total 59 - 58 split)
[]Store all this formate in pickle formate for futture use in DATA directory
"""

#1 main data pikle 

import shutil
from cv2 import CV_32F
import numpy as np
import random
import os
import cv2
import pickle
import matplotlib.pyplot as plt
import glob

dir = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset\\all'


fileTrainName = 'C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\train_STEGGED_DATASET.pickle'
fileTestName = 'C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\test_STEGGED_DATASET.pickle'
fileValidName = 'C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\valid_STEGGED_DATASET.pickle'


all_file_name = [fileTrainName,fileTestName,fileValidName]
# Main_dir = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset'

#categories = ['NORMAL','STEGGED']
#fileNmame = 'C:\\Users\\pskavalekar\\Desktop\\Scripts\\DATA\\largeSTEGGED_DATASET.pickle'
#data = []

"""
for category in categories:
    path = os.path.join(dir,category)
    label = categories.index(category)
    print(label,' ',category)
    for img in os.listdir(path):
        imgpath = os.path.join(path,img)
        item_img = cv2.imread(imgpath)
        item_img = cv2.resize(item_img,(1000,1000))
        data.append([item_img,label])

random.shuffle(data)

pickle_write = open(fileNmame,'wb')
pickle.dump(data,pickle_write)
pickle_write.close()
print('done')
"""



"""
os.chdir(dir)
if os.path.isdir(dir) is True:
    os.makedirs(os.path.join(dir,"train\\NORMAL"))
    os.makedirs(os.path.join(dir,"train\\STEGGED"))
    os.makedirs(os.path.join(dir,"test\\NORMAL"))
    os.makedirs(os.path.join(dir,"test\\STEGGED"))
    os.makedirs(os.path.join(dir,"valid\\NORMAL"))
    os.makedirs(os.path.join(dir,"valid\\STEGGED"))

print("done")
"""
train_path = os.path.join(dir,"train")
test_path = os.path.join(dir,"test")
valid_path = os.path.join(dir,"valid")

all_path = [train_path,test_path,valid_path]

categories = ['NORMAL','STEGGED']

"""
for c in random.sample(glob.glob('cap *'), 468):
    shutil.move(c,train_path_normal)
for c in random.sample(glob.glob('stegged *'), 468):
    shutil.move(c,train_path_stegged)
for c in random.sample(glob.glob('cap *'), 59):
    shutil.move(c,test_path_normal)
for c in random.sample(glob.glob('stegged *'), 58):
    shutil.move(c,test_path_stegged)
for c in random.sample(glob.glob('cap *'), 58):
    shutil.move(c,valid_path_normal)
for c in random.sample(glob.glob('stegged *'), 59):
    shutil.move(c,valid_path_stegged)

print("done")



#for converting image data and wrtiting it in pickle type

for one_path in all_path:

    data = []
    file_index = all_path.index(one_path)
    for category  in categories:
        path = os.path.join(one_path,category)
        label = categories.index(category)
        print(label,' ',categories[label],' ',one_path)

        for img in os.listdir(path):
            imgpath = os.path.join(path,img)
            item_img = cv2.imread(imgpath)
            item_img = cv2.resize(item_img,(1000,1000))
            data.append([item_img,label])
    

    random.shuffle(data)
    pickle_write = open(all_file_name[file_index],'wb')
    pickle.dump(data,pickle_write)
    print(all_file_name[file_index]," file created!")
    pickle_write.close()


"""
pickle_read = open(all_file_name[0],'rb') #reading the pickle data
data = pickle.load(pickle_read)
pickle_read.close()



