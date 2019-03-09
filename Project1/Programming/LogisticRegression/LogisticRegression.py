"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from math import exp

def convertStringToFloat(data, column):
    for line in data:
        line[column] = float(line[column])
        
#find mini and max values in the datset
def minMax(data):
    minmax = list()
    for i in range(len(data[0])):
        columnValues = [line[i] for line in data ]
        minValue = min(columnValues)
        maxValue = max(columnValues)
        minmax.append([minValue, maxValue])
    return minmax

#normalize the data set
def normalizeDataset(data, minmax):
    for line in data:
        for k in range(len(line)):
            line[k] = (line[k] - minmax[k][0])/(minmax[k][1] - minmax[k][0])
            
#value returned for Gender prediction            
def predictResult(row, coEfficients):
    yResult = coEfficients[0]
    for i in range(len(row)-1):
        yResult += coEfficients[i+1] * row[i]
    return 1.0/(1.0 + exp(-yResult))

#find the coefficients
def coEfficient_StochasticGD(trainingData, learning_rate, epochs):
    coEff = [0.0 for i in range(len(trainingData[0]))]
    for e in range(epochs):
        errorSum = 0
        for row in trainingData:
            yResult = predictResult(row,coEff)
            error = row[-1] - yResult
            errorSum += error**2
            coEff[0] = coEff[0] + learning_rate*error*yResult*(1.0 - yResult)
            for l in range(len(row) - 1):
                coEff[l+1] = coEff[l+1] + learning_rate*error*yResult*(1.0-yResult)*row[l]
    return coEff

#peform linear regression with Stochastic Gradient Descent
def logisticRegression(trainData, testData, learningRate, epochVal):
    predictions = list()
    coEfficient = coEfficient_StochasticGD(trainData, learningRate, epochVal)
    print('CoEfficients : ',coEfficient)
    for line in testData:
        yResult = predictResult(line, coEfficient)
        yResult = round(yResult)
        predictions.append(yResult)
    return predictions
            
if __name__ == '__main__':
    
    learningRate = 0.1
    epochValue = 100

    #considering '0' for Women and  '1' for Men
    trainingDataset = [[170,57,32,0],[192,95,28,1],[150,45,30,0],[170,65,29,1],[175,78,35,1],[185,90,32,1],[170,65,28,0],[155,48,31,0],[160,55,30,0],[182,80,30,1],[175,69,28,0],[180,80,27,1],[160,50,31,0],[175,72,30,1]]
    #testDataset = loadCSVFile(testCSVFileName)
    
    # convert integer values to float
    for n in range(len(trainingDataset[0])):
        convertStringToFloat(trainingDataset, n)
    
    #normalize the training data
    trainingDataMinMax = minMax(trainingDataset)
    normalizeDataset(trainingDataset, trainingDataMinMax)
    
    testDataset = [[155,40,35,0],[170,70,32,1],[175,70,35,0],[180,90,20,1]]
    
    # convert integer values to float
    for m in range(len(testDataset[0])):
        convertStringToFloat(trainingDataset, m)
        
    #normalize the test data
    testDataMinMax = minMax(testDataset)
    normalizeDataset(testDataset, testDataMinMax)
    
    predictions = logisticRegression(trainingDataset, testDataset, learningRate, epochValue)
    
    gender = ''
    
    for i in predictions:
        if predictions[i] == 0:
            gender = 'W'
        else:
            gender = 'M'
        print ('Prediction for test data : ', gender) 