"""
@author: sundesh raj
UTA_ID : 1001633297
"""
from csv import reader
from math import exp
import numpy as np

def loadCSV(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

#convert the dataset values to float
def convertStringToFloat(data, column):
    for line in data:
        line[column] = float(line[column])

def coEfficient_StochasticGD(trainingData, lRate, epochVal):
    coEff = [0.0 for i in range(len(trainingData[0]))]
    for e in range(epochVal):
        errorSum = 0
        for row in trainingData:
            yResult = predictResult(row,coEff)
            error = row[-1] - yResult
            errorSum += error**2
            coEff[0] = coEff[0] + lRate*error*yResult*(1.0 - yResult)
            for l in range(len(row) - 1):
                coEff[l+1] = coEff[l+1] + lRate*error*yResult*(1.0-yResult)*row[l]
        return coEff

def predictResult(row, coEff):
    yResult = coEff[0]
    for i in range(len(row)-1):
        yResult += coEff[i+1] * row[i]
    return 1.0/(1.0 + exp(-yResult))

def adaBoost(trainingData, lRate, epochVal, sample_weight, targetValues, nBoostSize):
    
    for size in range(nBoostSize):
        predictions = list()
        est_error,est_weight = [],[]
        initialCoEfficients = coEfficient_StochasticGD(trainingData, lRate, epochVal)
        incorrect = []
        incorrectIndexes = []
        
        for n in range(len(trainingData)):
            pred = predictResult(trainingData[n], initialCoEfficients)
            predictions.append(round(pred))
        for k in range(len(predictions)):
            if predictions[k] != targetValues[k]:
                incorrectIndexes.append(k)
                incorrect.append(False)
            else:
                incorrect.append(True)
        est_error = np.mean(np.average(incorrect, weights=sample_weight, axis=0))
        est_weight = learningRate * np.log((1. - est_error) / est_error)
        sample_weight *= np.exp(est_weight * ((sample_weight>0)|(est_weight<0)))
        
        for row in trainingData:
            for p in range(len(trainingData)):
                for i in range(len(row)-1):
                    if p in incorrectIndexes:
                        #add new sample weight to the incorrect data samples
                        trainingData[p][i] = trainingData[p][i] + sample_weight[i]
                    else:
                        trainingData[p][i] = trainingData[p][i]
    return trainingData

if __name__ == '__main__':
    
    learningRate = 1
    epochValue = 100
    
    #Note: Considered 0 for fake note and 1 for authentic note
    trainingDataFile = "train.csv"
    trainingDataSet = loadCSV(trainingDataFile)
    
    for n in range(len(trainingDataSet[0])):
        convertStringToFloat(trainingDataSet, n)
    
    testDataFile = "test.csv"
    testDataSet = loadCSV(testDataFile)
    
    for n in range(len(testDataSet[0])):
        convertStringToFloat(testDataSet, n)
    
    y = [int(row[-1]) for row in trainingDataSet]
    sample_weight = np.ones(len(trainingDataSet)) / len(trainingDataSet)
    
    print('=====================================================')
    print('Performing AdaBoost on Logistic Regression Classifier')
    print('=====================================================')
    print('\n')
    
    for boostSize in [1, 10, 25, 50]:
        
        boostedTrainingData = adaBoost(trainingDataSet, learningRate, epochValue, sample_weight, y, boostSize)
        print('Boost Size : ', boostSize)
        freshCoEff = coEfficient_StochasticGD(boostedTrainingData, learningRate, epochValue)
        print(freshCoEff)
        newPredictions = list()
        for n in range(len(testDataSet)):
            humma = predictResult(testDataSet[n], freshCoEff)
            newPredictions.append(round(humma))
        
        unit = 0
        for n in range(len(testDataSet)):
            if newPredictions[n] == int(testDataSet[n][4]):
                unit += 1
        
        for n in range(len(testDataSet)):
            print('Actual : ',int(testDataSet[n][4]), ' Predicted : ',newPredictions[n])
        accuracy = unit*100/len(testDataSet)
        print('Accuracy : ',accuracy)
        print('\n')