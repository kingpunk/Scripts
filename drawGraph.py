
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

large_name = 'internet set large.csv'
mid_name ='internet set mid.csv'
small_name = 'internet set small.csv'


df_large = pd.read_csv('classifiers\\mlp\\jupyter Notebook\\internet set\\dct\\'+large_name)
df_mid = pd.read_csv('classifiers\\mlp\\jupyter Notebook\\internet set\\dct\\'+mid_name)
df_small = pd.read_csv('classifiers\\mlp\\jupyter Notebook\\internet set\\dct\\'+small_name)


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
    fig, (plt1,plt2) = plt.subplots(1,2,figsize=(10,10))

    predictedNormal = seprateValue(valuesNormalDataframe)
    predictedNormal = preProccing(predictedNormal)
    valuesNormal = np.array(predictedNormal)
    totalN = sum(valuesNormal)
    print(valuesNormal)
    labels = ["knn","svm","DT","RF","MLP","Stack"]
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

    
    plt.show()


df = pd.concat([df_large.set_index('classifiers'),df_mid.set_index('classifiers'),df_small.set_index('classifiers')],axis=1)

df.plot.bar()
plt.xticks(rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc='best')
plt.show()



formatedPieChartValue(valuesRatioLargeNormalPredicted,valuesRatioLargeStaggedPredicted,title="Large set")
formatedPieChartValue(valuesRatioMidNormalPredicted,valuesRatioMidStaggedPredicted,title="Medium  set")
formatedPieChartValue(valuesRatioSmallNormalPredicted,valuesRatioSmallStaggedPredicted,title="Small Set")

