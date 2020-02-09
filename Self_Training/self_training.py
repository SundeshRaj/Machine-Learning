"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from math import exp
import csv


# Load a CSV file
def loadCSVFile(fileName):
    trainingData = list()
    inputFile = open(fileName, 'r')
    fileData = csv.reader(inputFile)
    for row in fileData:
        if not row:
            continue
        trainingData.append(row)
    return trainingData


# Convert string column to float
def convertStringToFloat(trainingData, column):
    for row in trainingData:
        row[column] = float(row[column].strip())


# Find the min and max values for each column
def minMax(trainingData):
    minmax = list()
    for i in range(len(trainingData[0])):
        colValues = [row[i] for row in trainingData]
        minValue = min(colValues)
        maxValue = max(colValues)
        minmax.append([minValue, maxValue])
    return minmax


# Rescale trainingData columns to the range 0-1
def normalizeDataset(trainingData, minmax):
    for row in trainingData:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


# Estimate logistic regression coefficients using stochastic gradient descent
def coEfficient_StochasticGD(trainingData, learningRate, n):
    coef = [0.0 for i in range(len(trainingData[0]))]
    for epoch in range(n):
        sumError = 0
        for row in trainingData:
            a = predictResult(row, coef)
            error = row[-1] - a
            sumError += error ** 2
            coef[0] = coef[0] + learningRate * error * a * (1.0 - a)
            for i in range(len(row)-1):
                coef[i + 1] = coef[i + 1] + learningRate * error * a * (1.0 - a) * row[i]
    return coef

# Make a prediction with coefficients
def predictResult(row, coefficients):
    a = coefficients[0]
    for i in range(len(row)-1):
        a += coefficients[i + 1] * row[i]
    return 1.0 / (1.0 + exp(-a))

count = 0
fileName = 'trainingData.csv'
trainingData = loadCSVFile(fileName)

testfile = 'testData.csv'
testData = loadCSVFile(testfile)

testfile1 = 'testData.csv'
testData1 = loadCSVFile(testfile1)

for i in range(len(trainingData[0])):
    convertStringToFloat(trainingData, i)

for i in range(len(testData[0])):
    convertStringToFloat(testData, i)

learningRate = 0.3
n = 100

#normalize traning data
minmax = minMax(trainingData)
normalizeDataset(trainingData, minmax)

#normalize test data
minmax = minMax(testData)
normalizeDataset(testData, minmax)

coef = coEfficient_StochasticGD(trainingData, learningRate, n)


for line1, line2 in zip(testData, testData1):
    ans = predictResult(line1, coef)
    print(ans)
    line2.append(round(ans))

    with open("trainingData.csv", "a") as ty:
        if count == 0:
            wr = csv.writer(ty)
            #wr.writerow([])
            wr.writerow(line2)
            count = 1
        elif count != 0:
    	    wr = csv.writer(ty)
    	    wr.writerow(line2)

    fname = 'trainingData.csv'
    trainingData = loadCSVFile(fname)

    for i in range(len(trainingData[0])):
    	convertStringToFloat(trainingData, i)

    minmax = minMax(trainingData)
    normalizeDataset(trainingData, minmax)
    coef = coEfficient_StochasticGD(trainingData, learningRate, n)