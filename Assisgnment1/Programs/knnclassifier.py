"""
@author: sundesh raj
UTA_ID : 1001633297
"""
import csv
import sys
import operator
import math

#laad the csv file and prepare the traning set
def loadCSVFile(filename, training=[]):

    csvdata = open(filename, 'r')
    data = csv.reader(csvdata)
    dataset = list(data)
    for instance in range(len(dataset)):
        for features in range(len(dataset[instance]) - 1):
            dataset[instance][features] = float(dataset[instance][features])
        if 1 == 1:
            training.append(dataset[instance])

#calcuate the distance between given 2 points
def calculateDistance(instance1, instance2, length):
    
    dis = 0
    for x in range(length):
        dis += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(dis)


#get the nearest neighbours for the input data
def findNeighbours(training, testInstance, k):

    distances = []
    length = len(testInstance)
    for instance in training:
        dist = calculateDistance(testInstance, instance, length)
        print ('Distance from %s to %s = %f' %(testInstance, instance, dist))
        distances.append((instance, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for instance in range(k):
        neighbours.append(distances[instance][0])
    return neighbours

#perform the gender prediction
def predictGender(neighbours):
    
    classes = {}
    for neighbour in neighbours:
        currClass = neighbour[-1]
        if currClass in classes:
            classes[currClass] += 1
        else:
            classes[currClass] = 1
    sortedClass = sorted(classes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClass[0][0]# returns 'M' for Man and 'W' for Woman

#classifies the input with respect to the traning data and starts the predictions and returns the output
def knnClassifier(X, test, k):
    
    print('k: ' + repr(k))
    neighbours = findNeighbours(X, test, k)
    prediction = predictGender(neighbours)
    return prediction
    
if __name__ == '__main__':
    
    #command line arguments
    csvFile = sys.argv[1]
    height = int(sys.argv[2])
    weight = int(sys.argv[3])
    age = int(sys.argv[4])
    k = int(sys.argv[5])
    X = []  # Training set
    loadCSVFile(csvFile, X)
    print('Predicted class: ' + knnClassifier(X, [height,weight,age], k))