

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


internetlarge_name = 'internet set large.csv'
interentmid_name ='internet set mid.csv'
internetsmall_name = 'internet set small.csv'

semilarge_name = "semi-captured large.csv"
semimid_name =  "semi-captured mid.csv"
semismall_name = "semi-captured small.csv"

capturedlarge_name = "captured datalarge.csv"
capturedmid_name = "captured datamid.csv"
capturedsmall_name = "captured datasmall.csv"

all_name_large = [capturedlarge_name,semilarge_name,internetlarge_name]
all_name_mid = [capturedmid_name,semimid_name,interentmid_name]
all_name_small = [capturedsmall_name,semismall_name,internetsmall_name]


datasetType = ['captured data','semi-captured','internet set']


algorithm = ['lsb','lsbran','dct']


original_path = 'C:\\Users\\kaval\\Documents\\University of plymouth - Masters Project\\Scripts\\classifiers\\mlp\\jupyter Notebook\\'


datasetIndex = 1
all_name_index = 1
algorithIndex = 0

dataset_path = os.path.join(original_path,datasetType[datasetIndex])
algorithmPath = os.path.join(dataset_path,algorithm[algorithIndex])


print(algorithmPath)

df_large = pd.read_csv(os.path.join(algorithmPath,all_name_large[all_name_index]))
df_mid = pd.read_csv(os.path.join(algorithmPath,all_name_mid[all_name_index]))
df_small = pd.read_csv(os.path.join(algorithmPath,all_name_small[all_name_index]))

print(os.path.join(algorithmPath,all_name_small[all_name_index]))

print(df_small)
predicted_to_normal_ratio = 'Predicted Normal / Actual  Normal Images'
predicted_to_stagg_ratio = 'Predicted stagged / Actual  Stagged Images'


valuesRatioLargeNormalPredicted = df_large[predicted_to_normal_ratio].values.tolist()
valuesRatioLargeStaggedPredicted = df_large[predicted_to_stagg_ratio].values.tolist()

valuesRatioMidNormalPredicted = df_mid[predicted_to_normal_ratio].values.tolist()
valuesRatioMidStaggedPredicted = df_mid[predicted_to_stagg_ratio].values.tolist()

valuesRatioSmallNormalPredicted = df_small[predicted_to_normal_ratio].values.tolist()
valuesRatioSmallStaggedPredicted = df_small[predicted_to_stagg_ratio].values.tolist()

def seprateValue(valueslist):
    values = []
    actual = []
    for val in valueslist:
        splitlist = val.split('/')
        values.append(int(splitlist[0]))
        actual.append(int(splitlist[1]))
    
    return values


def preProccing(values):
    final_val = []
    for val in values:
        if val == 58:
            val = val + 2
        elif val == 59:
            val = val + 1
        elif val == 61:
            val = val - 1
        final_val.append(val)
    return final_val

def formatedPieChartValue(valuesNormalDataframe,valuesStaggedDataFrame,title):
    #fig, (plt1,plt2) = plt.subplots(1,2,figsize=(10,10))
    
    labels = ["knn","svm","DT","RF","MLP","Stack"]
    predictedNormal = seprateValue(valuesNormalDataframe)
    predictedNormal = preProccing(predictedNormal)
    valuesNormal = np.array(predictedNormal)
    totalN = sum(valuesNormal)
    #print(valuesNormal)
    
    predictedStagged = seprateValue(valuesStaggedDataFrame)
    predictedStagged = preProccing(predictedStagged)
    valuesStagged = np.array(predictedStagged)
    totalS = sum(valuesStagged)
    #print(valuesStagged)
    

    fig = plt.figure(facecolor="white")

    ax = fig.add_subplot(1, 1, 1)
    bar_width = 0.5
    bar_l = np.arange(1, 7)
    tick_pos = [i + (bar_width / 2) for i in bar_l]

    ax1 = ax.bar(bar_l, valuesNormal, width=bar_width, label="Normal", color="green")
    ax2 = ax.bar(bar_l, valuesStagged, bottom=valuesNormal, width=bar_width, label="Stegged", color="blue")
    ax.set_ylabel("Accurate Predictions", fontsize=18)
    ax.set_xlabel("Classifiers", fontsize=18)
    ax.legend(loc="best")
    ax.set_ylim([0,120])
    plt.xticks(tick_pos, labels, fontsize=16)
    plt.yticks(fontsize=16)

    for r1, r2 in zip(ax1, ax2):
        h1 = r1.get_height()
        h2 = r2.get_height()
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1, ha="center", va="center", color="black", fontsize=16, fontweight="bold")
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="black", fontsize=16, fontweight="bold")
        
    plt.title("Predictions Made by classifiers on test "+title)
    plt.show()
    
    """labels = ["knn","svm","DT","RF","MLP","Stack"]
    plt1.pie(valuesNormal,labels=labels, autopct=lambda p: '{:.0f}'.format(p * totalN / 100))
    plt1.set_title("Normal "+title+" Prediction")
    plt1.legend(title="Classifiers",loc="best")

    predictedStagged = seprateValue(valuesStaggedDataFrame)
    predictedStagged = preProccing(predictedStagged)
    valuesStagged = np.array(predictedStagged)
    totalS = sum(valuesStagged)
    print(valuesStagged)
    labels = ["knn","svm","DT","RF","MLP","Stack"]
    plt2.pie(valuesStagged,labels=labels, autopct=lambda p: '{:.0f}'.format(p * totalS / 100))
    plt2.set_title("Stagged "+title+" Prediction")
    plt2.legend(title="Classifiers",loc="best")

    
    plt.show()"""




#df = pd.concat([df_large.set_index('classifiers'),df_mid.set_index('classifiers'),df_small.set_index('classifiers')],axis=1)


def drawbarChart(dfchart,title):
    labels = ["KNN","SVM","DT","RF","MLP","Stack"]
    ax = dfchart.plot(kind='bar',edgecolor='white', linewidth=5)
    
    ran = np.arange(6)
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))   
    plt.xticks(ran,labels=labels,rotation=0,fontsize=15)
    plt.ylim(0,1.2)
    plt.legend(loc='best')
    plt.xlabel("Classifiers",fontsize=18)
    plt.ylabel("Performance",fontsize=18)
    plt.title(title+" Classification Performance")
    plt.show()



#make data frame in 2 decimal

def preProcessing(df,size):
    
    df['Accuracy '+size] = df['Accuracy '+size].round(decimals = 2)
    df['MCC '+size]=df['MCC '+size].round(decimals = 2)
    df['F1-score '+size] = df['F1-score '+size].round(decimals = 2)
    return df


df_large = preProcessing(df_large,size='Large')
df_mid = preProcessing(df_mid,size='Mid')
df_small = preProcessing(df_small,size='small')
#print(df_large)
#print(df_mid)
#print(df_small)

drawbarChart(dfchart=df_large,title="Large set")
formatedPieChartValue(valuesRatioLargeNormalPredicted,valuesRatioLargeStaggedPredicted,title="Large set")

drawbarChart(dfchart=df_mid,title="Medium set")
formatedPieChartValue(valuesRatioMidNormalPredicted,valuesRatioMidStaggedPredicted,title="Medium  set")


drawbarChart(dfchart=df_small,title="Small set")
formatedPieChartValue(valuesRatioSmallNormalPredicted,valuesRatioSmallStaggedPredicted,title="Small Set")








"""

#print(plt.__version__)

"""