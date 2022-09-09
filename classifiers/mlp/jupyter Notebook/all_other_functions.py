import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import os
import cv2
from tensorflow.python.keras.metrics import BinaryAccuracy
from tensorflow.python.keras.models import load_model
import warnings
warnings.filterwarnings("ignore")


def readPickledata(filelocation):
    pickel_read = open(filelocation,'rb')
    data = pickle.load(pickel_read)
    pickel_read.close()
    return data


def writePickledata(filelocation,data):
    pickel_write = open(filelocation,'wb')
    pickle.dump(data,pickel_write)
    pickel_write.close()
    print('file writing done')


def load_save_models(modelLocation):
    return load_model(modelLocation)


def draw_Training_validation_loss(history,title):
    #Training and validation Loss
    loss = history['loss']
    val_loss = history['val_loss']
    epochs = range(1,len(loss)+1)
    plt.plot(epochs,loss,'yo',label='Training Loss')
    plt.plot(epochs,val_loss,'r',label='Validation Loss')
    plt.legend("TVloss")
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.show()

def draw_Trainingvalidation_acc(history,title):
    #Training and validation accuracy
    accuracy = history['accuracy']
    val_acc = history['val_accuracy']
    epochs = range(1,len(accuracy)+1)
    plt.plot(epochs,accuracy,'yo',label='Training acc')
    plt.plot(epochs,val_acc,'r',label='Validation acc')
    plt.legend("TVacc")
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()

def returnCount(data):
    normal = 0
    steg = 0

    for categorie in data:
        if categorie == 0:
            normal=normal+1
        elif categorie == 1:
            steg = steg +1
    return normal,steg

def add_value_label(x_list,y_list):
    for i in range(0, len(x_list)):
        plt.text(i,y_list[i],y_list[i], ha="center")
    
def correctPredictedValue(data,predicted):
    normal = 0
    stagged = 0

    if len(data) == len(predicted):
        i = 0
        while i < len(data):
            if data[i] == predicted[i] == 1:
                stagged = stagged + 1
            if data[i] == predicted[i] == 0:
                normal = normal + 1

            i=i+1
    
    return normal,stagged

    
def drawchart(data,predicted_data):
    
    
    
    actual_result_normal,actual_result_stegg = returnCount(data)
    predicted_normal_count, predicted_steg_count = correctPredictedValue(data,predicted_data) 
    
    normal_actual_and_predicted_list = [predicted_normal_count,actual_result_normal]
    stagg_actual_and_predicted_list = [predicted_steg_count,actual_result_stegg]
    """
    should_be_result = np.array([actual_result_normal,actual_result_stegg])
    predicted_result = np.array([predicted_normal_count,predicted_steg_count])
    plt.title("original values")
    plt.bar(categoies,should_be_result,color=['blue','red'])
    add_value_label(categoies,should_be_result)
    plt.show()

    plt.bar(categoies,predicted_result,color=['blue','red'])
    add_value_label(categoies,predicted_result)
    plt.title("predicted values")
    plt.show()"""
    return normal_actual_and_predicted_list, stagg_actual_and_predicted_list

def drawhistrogram(features,labels):
    random_image_value = random.randint(0,len(features))
    plt.plot(features[random_image_value,:])
    if labels[random_image_value] == 0:
        plt.title("Normal")
    else:
        plt.title("stegged")
    plt.show()
    return random_image_value


def showImage(fileLocation):
    image = cv2.imread(fileLocation,0)
    image = cv2.resize(image,(250,250))
    cv2.imshow('model image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def accuracyPredrict(y_true,y_predict):
    metric = BinaryAccuracy(threshold=0.5)
    metric.update_state(y_true,y_predict)
    metric = np.array(metric.result())
    return metric


def typeOfDataset(dataset):
    if dataset == 'train':
        return 'training set'
    elif dataset == 'test':
        return 'testing set'
    elif dataset == 'valid':
        return 'validation set'
    elif dataset == 'internet':
        return 'Internet set'
    elif dataset == 'small':
        return 'small set '


def createReport(predictedValue,predictedClasses,trueValue):
    report = ''

    #f'Test results - Loss: {test_results[0]*100} - Accuracy: {test_results[1]*100}%'

    if len(predictedValue) == len(predictedClasses) == len(trueValue):
        counter = 0  #used for incrementing in other variable
        for value in predictedValue:
            imagenumer = str(counter+1)
            #print("imagenumber"+imagenumer)
            #print("counter",counter)
            if trueValue[counter] == 0:
                true_image_statues = 'normal'
            elif trueValue[counter] == 1:
                true_image_statues = 'stegged'
            
            probability_of_image = str(value[0] * 100) + "%"
            
            if predictedClasses[counter][0] == 0:
                predicted_image_class = 'normal'
            elif predictedClasses[counter][0] == 1:
                predicted_image_class = 'stegged'
                
            report = report +'\n True value of image '+imagenumer+' is '+true_image_statues+' predicted class is '+ predicted_image_class + ' with value '+ probability_of_image
            counter = counter + 1
    
    print(report)
        
            

def pathExists(path):
    if os.path.exists(path):
        print("Yes")
    else:
        print(path)
        print("No")     


def returnStringCombined(predicted,actual):
    stringPredicted = str(predicted)
    stringActual =str(actual)
    combine = stringPredicted + '/' + stringActual
    return combine