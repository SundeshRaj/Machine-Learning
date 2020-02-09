"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from math import exp
import csv


# Load a CSV file
def loadCSVFile(trainingDataSetFile):
    trainingDataSet = list()
    inputFile = open(trainingDataSetFile, 'r')
    fileData = csv.reader(inputFile)
    for line in fileData:
        if not line:
            continue
        trainingDataSet.append(line)
    return trainingDataSet


# Convert string column to float
def convertStringToFloat(trainingDataSet, column):
    for line in trainingDataSet:
        line[column] = float(line[column].strip())


# Find the min and max values for each column
def minMax(trainingDataSet):
    minmax = list()
    for k in range(len(trainingDataSet[0])):
        column = [row[k] for row in trainingDataSet]
        minValue = min(column)
        maxValue = max(column)
        minmax.append([minValue, maxValue])
    return minmax


# Rescale trainingDataSet columns to the range 0-1
def normalizeDataset(trainingDataSet, minmax):
    for row in trainingDataSet:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


# Make a prediction with coefficients
def predictResult(row, coefficients):
    y_result = coefficients[0]
    for i in range(len(row) - 1):
        y_result += coefficients[i + 1] * row[i]
    return 1.0 / (1.0 + exp(-y_result))


# Estimate logistic regression coefficients using stochastic gradient descent
def coEfficient_StochasticGD(trainingDataSet, learningRate, n):
    coEfficient = [0.0 for i in range(len(trainingDataSet[0]))]
    for epoch in range(n):
        sumError = 0
        for row in trainingDataSet:
            y_result = predictResult(row, coEfficient)
            er = row[-1] - y_result
            sumError += er ** 2
            coEfficient[0] = coEfficient[0] + learningRate * er * y_result * (1.0 - y_result)
            for i in range(len(row) - 1):
                coEfficient[i + 1] = coEfficient[i + 1] + learningRate * er * y_result * (1.0 - y_result) * row[i]
    return coEfficient


trainingDataSetFile = 'trainingData.csv'
trainingDataSet = loadCSVFile(trainingDataSetFile)

testDataFile = 'testData.csv'
selfLearningData = loadCSVFile(testDataFile)

testDataFile1 = 'testData.csv'
selfLearningData1 = loadCSVFile(testDataFile1)

for i in range(len(trainingDataSet[0])):
    convertStringToFloat(trainingDataSet, i)

for i in range(len(selfLearningData[0])):
    convertStringToFloat(selfLearningData, i)

numErrors = 0
occurrances = 0
numErrors2 = 0
occurrances2 = 0
count = 0
lRate = 0.1
epochValue = 100

labelledTestData = [[169.0, 58.0, 30.0, 1.0],[185.0, 90.0, 29.0, 0.0],[148.0, 40.0, 31.0, 1.0],[177.0, 80.0, 29.0, 0.0],[170.0, 62.0, 27.0, 1.0],[172.0, 72.0, 30.0, 0.0],[175.0, 68.0, 27.0, 1.0],[178.0, 80.0, 29.0, 1.0]]

unlabelledTestData = [[169.0, 58.0, 30.0],[185.0, 90.0, 29.0],[148.0, 40.0, 31.0],[177.0, 80.0, 29.0],[170.0, 62.0, 27.0],[172.0, 72.0, 30.0],[175.0, 68.0, 27.0],[178.0, 80.0, 29.0]]

# normalize traning data
minmax = minMax(trainingDataSet)
normalizeDataset(trainingDataSet, minmax)

# normalize test data
minmax = minMax(labelledTestData)
normalizeDataset(labelledTestData, minmax)

# normalize learn data
minmax = minMax(selfLearningData)
normalizeDataset(selfLearningData, minmax)

coef = coEfficient_StochasticGD(trainingDataSet, lRate, epochValue)

print ("\n")
print ("Supervised Learning Implementation:")
for row in labelledTestData:
    ans = predictResult(row, coef)
    occurrances = occurrances + 1
    if round(ans) == 1 and round(row[-1]) == 1:
        print ("Predicted Class = W")
    elif round(row[-1] == 1) and round(ans) == 0:
        numErrors = numErrors + 1
        print ("Predicted Class = M")
    elif round(row[-1] == 0) and round(ans) == 0:
        print ("Predicted Class = M")
    elif round(row[-1] == 0) and round(ans) == 1:
        numErrors = numErrors + 1
        print ("Predicted Class = W")


supervisedAccuracy = ((occurrances - numErrors) * 100) / occurrances

print("Supervised Learning Accuracy : ", supervisedAccuracy,"%")

for nLine, mLine in zip(selfLearningData, selfLearningData1):
    ans = predictResult(nLine, coef)
    mLine.append(round(ans))

    with open("trainingData.csv", "a") as mQ:
        if count == 0:
            csvWrite = csv.writer(mQ)
            csvWrite.writerow([])
            csvWrite.writerow(mLine)
            count = 1
        elif count != 0:
            csvWrite = csv.writer(mQ)
            csvWrite.writerow(mLine)

    fileName = 'trainingData.csv'
    trainingDataSet = loadCSVFile(fileName)

    for i in range(len(trainingDataSet[0])):
        convertStringToFloat(trainingDataSet, i)

    minmax = minMax(trainingDataSet)
    normalizeDataset(trainingDataSet, minmax)
    coef = coEfficient_StochasticGD(trainingDataSet, lRate, epochValue)

print ("\n")
print ("Semi-Supervised Learning Implementation:")
for nLine, mLine in zip(labelledTestData, unlabelledTestData):
    ans = predictResult(nLine, coef)
    mLine.append(round(ans))

    with open("trainingData.csv", "a") as mQ:
        if count == 0:
            csvWrite = csv.writer(mQ)
            csvWrite.writerow([])
            csvWrite.writerow(mLine)
            count = 1
        elif count != 0:
            csvWrite = csv.writer(mQ)
            csvWrite.writerow(mLine)

    fileName = 'trainingData.csv'
    trainingDataSet = loadCSVFile(fileName)

    for i in range(len(trainingDataSet[0])):
        convertStringToFloat(trainingDataSet, i)

    minmax = minMax(trainingDataSet)
    normalizeDataset(trainingDataSet, minmax)
    coef = coEfficient_StochasticGD(trainingDataSet, lRate, epochValue)

    occurrances2 = occurrances2 + 1
    if round(ans) == 1 and round(nLine[-1]) == 1:
        print ("Predicted Class = W")
    elif round(nLine[-1]) == 1 and round(ans) == 0:
        numErrors2 = numErrors2 + 1
        print ("Predicted Class = M")
    elif round(nLine[-1]) == 0 and round(ans) == 0:
        print ("Predicted Class = M")
    elif round(nLine[-1]) == 0 and round(ans) == 1:
        numErrors2 = numErrors2 + 1
        print ("Predicted Class = W")


semiSupervisedAccuracy = ((occurrances2 - numErrors2) * 100) / occurrances2

print("Semi-Supervised Learning Accuracy : ", semiSupervisedAccuracy,"%")