import numpy as np
import random
import os
import cv2
import pickle
import matplotlib.pyplot as plt


fileName='cnnModel.pickle'
#train_path = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\all-images-cnn\\train'
#test_path = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\all-images-cnn\\test'
"""

dir = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\CapturedDataset'
categories = ['NORMAL','STEGGED']
fileName='cnnModel.pickle'

data = []


for category in categories:
    path = os.path.join(dir,category)
    label = categories.index(category)
    print(label,'',category)
    for img in os.listdir(path):
        imgpath = os.path.join(path,img)
        item_img = cv2.imread(imgpath)
        item_img=cv2.resize(item_img,(100,100))
        data.append([item_img,label])

pickle_write = open(fileName,'wb')
pickle.dump(data,pickle_write)
pickle_write.close()
print('done')"""

pickle_read = open(fileName,'rb') #reading the pickle data
data = pickle.load(pickle_read)
pickle_read.close()

features = []
labels = []

for feature, label in data:
    features.append(feature)
    labels.append(label)

features=np.array(features)
labels=np.array(labels)

features = features/255
labels= labels.reshape(len(labels),1)

idx = random.randint(0,len(features))
plt.imshow(features[idx,:])
if labels[idx,:] == 0:
    plt.title("Normal")
else:
    plt.title("stegged")
plt.show()
#done