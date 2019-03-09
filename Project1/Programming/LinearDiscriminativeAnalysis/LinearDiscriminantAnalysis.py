"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from csv import reader
import numpy as np
import matplotlib.pyplot as plt

# Load a CSV file
def loadCSV(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

#convert input string values to float for calculation
def convertStringToFloat(data, column):
    for line in data:
        line[column] = float(line[column])
        
def getRandomValues(mean, pooledCovariance, num):
    result = []
    result = np.random.multivariate_normal(mean,pooledCovariance,num)
    return result


if __name__ == '__main__':
    
    learningDataFile = "data.csv"
    learningDataSet = loadCSV(learningDataFile)
    
    testDataFile = "testData.csv"
    testDataSet = loadCSV(testDataFile)
    
    learningDataWithoutLabel = []
    
    for p in range(len(testDataSet[0])):
        convertStringToFloat(testDataSet,p)
    
    for k in learningDataSet:
        learningDataWithoutLabel.append([k[0],k[1],k[2]])
        
    for k in range(len(learningDataWithoutLabel[0])):
        convertStringToFloat(learningDataWithoutLabel,k)
    
    dataSetMen = []
    for line in learningDataSet:
        if line[3] == 'M':
            dataSetMen.append([line[0],line[1],line[2]])
            
    for n in range(len(dataSetMen[0])):
        convertStringToFloat(dataSetMen,n)
            
    dataSetWomen = []
    for line in learningDataSet:
        if line[3] == 'W':
            dataSetWomen.append([line[0],line[1],line[2]])
            
    for n in range(len(dataSetWomen[0])):
        convertStringToFloat(dataSetWomen,n)
        
    probabilityOfMen = len(dataSetMen)/len(learningDataSet)
    probabilityOfWomen = len(dataSetWomen)/len(learningDataSet)
           
    menWeights = []     
    menHeights = []
    menAges = []
    for val in dataSetMen:
        menHeights.append(val[0])
        menWeights.append(val[1])
        menAges.append(val[2])
        
    #men mean values
    menMeanHeight = sum(menHeights)/len(menHeights)
    menMeanWeight = sum(menWeights)/len(menWeights)
    menMeanAge = sum(menAges)/len(menAges)
    
    menMean = []
    menMean.append(menMeanHeight)
    menMean.append(menMeanWeight)
    menMean.append(menMeanAge)
        
    womenWeights = []
    womenHeights = []
    womenAges = []
    for val in dataSetWomen:
        womenHeights.append(val[0])
        womenWeights.append(val[1])
        womenAges.append(val[2])
        
    #women mean values
    womenMeanHeight = sum(womenHeights)/len(womenHeights)
    womenMeanWeight = sum(womenWeights)/len(womenWeights)
    womenMeanAge = sum(womenAges)/len(womenAges)
    
    womenMean = []
    womenMean.append(womenMeanHeight)
    womenMean.append(womenMeanWeight)
    womenMean.append(womenMeanAge)
    
    allHeights = []
    allWeights = []
    allAges = []
    for val in learningDataWithoutLabel:
        allHeights.append(val[0])
        allWeights.append(val[1])
        allAges.append(val[2])
        
    allMeanHeight = sum(allHeights)/len(allHeights)
    allMeanWeight = sum(allWeights)/len(allWeights)
    allMeanAge = sum(allAges)/len(allAges)

    allMean = []
    allMean.append([allMeanHeight,allMeanWeight,allMeanAge])
    
    meanCorrectedMen = []
    for val in dataSetMen:
        meanCorrectedMen.append([val[0]-allMeanHeight,val[1]-allMeanWeight,val[2]-allMeanAge])
        
    meanCorrectedWomen = []
    for val in dataSetWomen:
        meanCorrectedWomen.append([val[0]-allMeanHeight,val[1]-allMeanWeight,val[2]-allMeanAge])
    
    coVarianceMatrixMen = (np.dot(np.transpose(meanCorrectedMen),meanCorrectedMen))/len(dataSetMen)
    coVarianceMatricWomen = (np.dot(np.transpose(meanCorrectedWomen),meanCorrectedWomen))/len(dataSetWomen)
    
    #calculating pooled group covariance
    coVarianceMatrixMen = coVarianceMatrixMen*probabilityOfMen
    coVarianceMatricWomen = coVarianceMatricWomen*probabilityOfWomen
    
    pooledGroupCoVariance = np.add(coVarianceMatrixMen,coVarianceMatricWomen)
    
    #f with respect to Men
    fMen = []
    for input in testDataSet:
        temp1 = np.dot(menMean,np.linalg.inv(pooledGroupCoVariance))
        temp2 = np.dot(temp1,np.transpose(input))
        temp3 = np.dot(menMean,np.linalg.inv(pooledGroupCoVariance))
        temp4 = np.dot(temp3,np.transpose(menMean))
        temp5 = temp4 * 0.5
        temp6 = temp2-temp5+np.log(probabilityOfMen)
        fMen.append(temp6)
    
    #f with respect to women
    fWomen = []
    for input in testDataSet:
        temp1 = np.dot(womenMean,np.linalg.inv(pooledGroupCoVariance))
        temp2 = np.dot(temp1,np.transpose(input))
        temp3 = np.dot(womenMean,np.linalg.inv(pooledGroupCoVariance))
        temp4 = np.dot(temp3,np.transpose(womenMean))
        temp5 = temp4 * 0.5
        temp6 = temp2-temp5+np.log(probabilityOfWomen)
        fWomen.append(temp6)
    
    #compare the f values and print the prediction
    for value in range(len(fMen)):
        if (fMen[value] > fWomen[value]):
            print('Prediction = M')
        else:
            print('Prediction = W')
            
    menRandomValues = getRandomValues(menMean,pooledGroupCoVariance,50)
    womenRandomValues = getRandomValues(womenMean,pooledGroupCoVariance,50)
    
    randomHeights = []
    randomWeights = []
    for line in menRandomValues:
        randomHeights.append(line[0])
        randomWeights.append(line[1])
    for line in womenRandomValues:
        randomHeights.append(line[0])
        randomWeights.append(line[1])
    
    print('\nMen Random Data : \n',menRandomValues)
    print('\nWomen Random Data : \n',womenRandomValues)
    
    #plot graph for training data
    plt.title("Training Data Heights vs Weights")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.plot(allHeights,allWeights, 'o')
    plt.show()
    
    #plot graph for random generated data
    plt.title("Random generated Heights vs weights")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.plot(randomHeights,randomWeights,'o')
    plt.show()
