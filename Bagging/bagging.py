"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from csv import reader
from random import randrange
from math import exp

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

#create similar size samples for the input data set (bags)
def createRandomSamples(dataset, ratio):
    sample = list()
    n_sample = round(len(dataset)*ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample
    
#find the SG CoEfficients with respect to the training data set
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

#class prediction sub function
def predictResult(row, coEff):
    yResult = coEff[0]
    for i in range(len(row)-1):
        yResult += coEff[i+1] * row[i]
    return 1.0/(1.0 + exp(-yResult))
    
#predict the class
def bagging_predict(row, sampleCoEfficients):
    predictions = list()
    for coEff in sampleCoEfficients:
        pred = predictResult(row, coEff)
        pred = round(pred)
        predictions.append(pred)
    return max(set(predictions), key=predictions.count)

#perform bagging
def bagging(trainingData, testData, numBags, ratio, lRate, epochVal):
    samples = list()
    for i in range(numBags):
        sample = createRandomSamples(trainingData, ratio)
        coEff = coEfficient_StochasticGD(sample, lRate, epochVal)
        samples.append(coEff)
    predictions = [bagging_predict(line, samples) for line in testData] 
    return(predictions)

if __name__ == '__main__':
    
    learningRate = 0.3
    epochValue = 100
    ratio = 1.0
    
    #Note: Considered 0 for fake note and 1 for authentic note
    trainingDataFile = "train.csv"
    trainingDataSet = loadCSV(trainingDataFile)
    
    for n in range(len(trainingDataSet[0])):
        convertStringToFloat(trainingDataSet, n)
    
    testDataFile = "test.csv"
    testDataSet = loadCSV(testDataFile)
    
    for n in range(len(testDataSet[0])):
        convertStringToFloat(testDataSet, n)

    print('====================================================')
    print('Performing Bagging on Logistic Regression Classifier')
    print('====================================================')
    print('\n')
    #perform bagging for different bag sizes
    for nBagSize in [1, 10, 50, 100]:
        pred = bagging(trainingDataSet, testDataSet, nBagSize, ratio, learningRate, epochValue)
        count = 0
        for n in range(len(testDataSet)):
            if pred[n] == int(testDataSet[n][4]):
                count += 1
        #calculating the accuracy based on the number of correct predictions
        accuracy = count*100/len(testDataSet)
        print('Num of Bags : ', nBagSize)
        for n in range(len(testDataSet)):
            print('Actual : ',int(testDataSet[n][4]), ' Predicted : ',pred[n])
        print('Accuracy : ', accuracy,'%')
        print('\n')