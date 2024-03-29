"""import random
import string


def generateRandomString(randomTextSize):

    lowerCaseLetters = string.ascii_lowercase
    uppderCaseLetters = string.ascii_uppercase
    letters= string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    all = [lowerCaseLetters,uppderCaseLetters,letters,digits,punctuations]

    
    text = ''

    for i in range(randomTextSize):
        text += ''.join([random.choice(i) for i in all])
    
    return text




print(generateRandomString(randomTextSize=100))

import glob
import os
import random
import shutil

path = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\all-images-cnn"
os.chdir(path)

if os.path.isdir(path) is True:
    os.chdir(path)
    os.makedirs("train\\normal")
    os.makedirs("train\\stegged")
    os.makedirs("test\\normal")
    os.makedirs("test\\stegged")
    print("working", path)



for c in random.sample(glob.glob('cap*'), 439):
    shutil.move(c,'train\\normal')
for c in random.sample(glob.glob('stegged*'), 439):
    shutil.move(c,'train\\stegged')
for c in random.sample(glob.glob('cap*'), 146):
    shutil.move(c,'test\\normal')
for c in random.sample(glob.glob('stegged*'), 146):
    shutil.move(c,'test\\stegged')

print(os.getcwd())



from sklearn.model_selection import train_test_split 

dir = 'C:\\Users\\pskavalekar\\Desktop\\DATASET\\CapturedDataset'

categories = ['NORMAL','STEGGED'] # categories of the data

data = []
for category in categories:
    path = os.path.join(dir,category)
    label = categories.index(category)
    print(label,'',category)
    for img in os.listdir(path):
        imagpath = os.path.join(path,img)
        item_img = cv2.imread(imagpath,cv2.IMREAD_GRAYSCALE)
        #cv2.imshow('image test',item_img)
        try:
            item_img = cv2.resize(item_img,(100,100))
            image = np.array(item_img)
            data.append([image,np.array(label)])
        except Exception as e:
            print("error"+e)
 

filename= 'cnnEncrypted_test_data.npy'
np.save(filename,data)


pickle_read = open(filename,'rb') #reading the pickle data
data = pickle.load(pickle_read)
pickle_read.close()


print(data)

#features = [] #color features of the images
#labels = [] #normal(0) or stegged(1)

#for feature, label in data:
 #   features.append(np.array(feature)) # [255,4,8] <- type of data
  #  labels.append(label) # 0, 1 ,0 type of data


#print(features)
#print(type(labels))


#labels=np.array(labels)
#features = features.reshape(len(features),100,100,3)
#labels = labels.reshape(len(labels),1)

#X_train, x_test, Y_train, y_test = train_test_split(features,labels,test_size=0.25)
"""
"""

import scriptforStegg as sc

total_size=(2176/8)*(4608/8)



print(total_size)

size = 100

while True:
    print("searhing with",size)
    lenOFSize= len(sc.generateRandomString(size))
    if (total_size-lenOFSize) < 10:
        print(lenOFSize)
        break
    else:
        print(total_size-lenOFSize)
        size = size + 100


lenOFsize = len(sc.generateRandomString(1000000))
print(lenOFsize)

"""

import importlib.util

spec = importlib.util.spec_from_file_location("all_other_functions","classifiers\\mlp\\jupyter Notebook\\all_other_functions.py")

foo = importlib.util.module_from_spec(spec)

spec.loader.exec_module(foo)


predicted_values = [0,0,0,0, 0 ,0, 1, 1, 0, 1, 0, 1, 1, 1, 1 ,0 ,1, 0 ,1, 1, 0, 1, 1, 1, 0 ,1 ,0 ,0, 1, 1, 0, 0 ,0 ,1 ,1, 0, 1]
actual_values = [1 ,1, 0 ,0 ,0 ,0 ,1 ,1 ,0, 1, 0 ,1 ,1 ,1 ,0 ,0 ,1, 0 ,1, 1, 0, 1 ,1 ,1 ,0, 1 ,0 ,0 ,1, 1, 0 ,0 ,0 ,1 ,1 ,0, 1]

normal_actual_and_predicted_list,stagg_actual_and_predicted_list = foo.drawchart(actual_values,predicted_values)

print("Predicted correct normal Values: "+ str(normal_actual_and_predicted_list[0]))
print("Actual normal Values: "+ str(normal_actual_and_predicted_list[1]))

print("Predicted correct stagged Values: "+ str(stagg_actual_and_predicted_list[0]))
print("Actual stagged Values: "+ str(stagg_actual_and_predicted_list[1]))