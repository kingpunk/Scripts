import os
from statistics import mode
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

"""dir = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\CapturedDataset'

categories = ['NORMAL','STEGGED'] # categories of the data

data = [] # to store the main data which will be used for testing



for category in categories:
    path = os.path.join(dir,category)
    label = categories.index(category) # getting the index of the category , this case  0 -> normal images , 1 -> stegged images

    for img in os.listdir(path):
        imgpath = os.path.join(path,img)
        item_img = cv2.imread(imgpath,0)
        #cv2.imshow('image test',item_img) #show the image test
        try:
           item_img = cv2.resize(item_img,(1000,1000))
           image = np.array(item_img).flatten() 
           data.append([image,label]) #adding image and label to the main data holder
        except Exception as e:
            raise ValueError("[!] "+ e)

pickle_write = open('svmMODELdata.pickle','wb')
pickle.dump(data,pickle_write)
pickle_write.close()
print('done')
    
#cv2.waitKey(0)
#cv2.destroyAllWindows()
"""

#Above section is commented bcoz, with the help from above section the data is stored in the pickle formate which i can use anytime, otherwise
#running the above section code each time consumes lot of memeory and time.

fileName = "svmMODELdata.pickle" 
 
pickle_read = open(fileName,'rb') #reading the pickle data
data = pickle.load(pickle_read)
pickle_read.close()

#random.shuffle(data) #can be used for blind steg where model will have mixture of both type of data (normal and stegged)

features = [] #color features of the images
labels = [] #normal(0) or stegged(1)

for feature, label in data:
    features.append(feature) # [255,4,8] <- type of data
    labels.append(label) # 0, 1 ,0 type of data
    
    
xtrain, xtest, ytrain, ytest = train_test_split(features,labels,test_size=0.25) 

"""
main data is divided into two parts - test size is 25% and train size will be 75% 
once training of the model is done with train data, test data will be used to check for the accuracy
"""

model = SVC(C=1,kernel='poly',gamma='auto')
model.fit(xtrain,ytrain)

prediction = model.predict(xtest)
accuracy = model.score(xtest,ytest)

categories = ['NORMAL','STEGGED']

print('Accuracy: ',accuracy)
print('Predction: ',categories[prediction[0]])

myImage=xtest[0].reshape(1000,1000)
plt.imshow(myImage,cmap='gray')
plt.show()