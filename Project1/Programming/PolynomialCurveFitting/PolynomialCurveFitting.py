"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from csv import reader
import numpy as np

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

if __name__ == '__main__':
    
    trainingDataFile = "data.csv"
    trainingDataSet = loadCSV(trainingDataFile)
    
    for p in range(len(trainingDataSet[0])):
        convertStringToFloat(trainingDataSet,p)
    
    testDataFile = "testData.csv"
    testDataSet = loadCSV(testDataFile)
    
    for p in range(len(testDataSet[0])):
        convertStringToFloat(testDataSet,p)
        
    trainingSetMatrixFirstDegree = []
    for line in trainingDataSet:
        trainingSetMatrixFirstDegree.append([1.0,line[0],line[1]])
        
    trainingYMatrix = []
    for line in trainingDataSet:
        trainingYMatrix.append([line[2]])
        
    thetaFirstDegree = []
    traininSetMatrixTransposeFirstDegree = np.transpose(trainingSetMatrixFirstDegree)
    temp = np.matmul(traininSetMatrixTransposeFirstDegree,trainingSetMatrixFirstDegree)
    temp = np.linalg.inv(temp)
    temp2 = np.matmul(temp, traininSetMatrixTransposeFirstDegree)
    thetaFirstDegree = np.matmul(temp2, trainingYMatrix)
    
    #print('First order polynomial coefficients : ', thetaFirstDegree)
    
    #test for 1st order polynomial
    print('\nFirst order polynomial predictions')
    for line in testDataSet:
        val = thetaFirstDegree[0]+thetaFirstDegree[1]*line[0]+thetaFirstDegree[2]*line[1]
        print('Actual value :',line[2],' Predicted value :',val,' ,Error = ',val-line[2])
    
    trainingSetMatrixSecondDegree = []
    for line in trainingSetMatrixFirstDegree:
        trainingSetMatrixSecondDegree.append([line[0],line[1],line[2],line[1]**2,line[2]**2,line[1]*line[2]])
        
    thetaSecondDegree = []
    trainingSetMatrixTransposeSecondDegree = np.transpose(trainingSetMatrixSecondDegree)
    tempSecondDegree = np.matmul(trainingSetMatrixTransposeSecondDegree,trainingSetMatrixSecondDegree)
    tempSecondDegree = np.linalg.inv(tempSecondDegree)
    temp2SecondDegree = np.matmul(tempSecondDegree, trainingSetMatrixTransposeSecondDegree)
    thetaSecondDegree = np.matmul(temp2SecondDegree, trainingYMatrix)
    
    #print('Second order polynomial coefficients : ',thetaSecondDegree)
    
    #test for second order polynomials
    print('\n\nSecond order polynomial predictions')
    for line in testDataSet:
        val2 = thetaSecondDegree[0]+thetaSecondDegree[1]*line[0]+thetaSecondDegree[2]*line[1]+thetaSecondDegree[3]*line[0]**2+thetaSecondDegree[4]*line[1]**2+thetaSecondDegree[5]*line[0]*line[1]
        print('Actual value : ',line[2],' Predicted value : ',val2,' ,Error = ',val2-line[2])
    
    trainingSetMatrixThirdDegree = []
    for line in trainingSetMatrixSecondDegree:
        trainingSetMatrixThirdDegree.append([line[0],line[1],line[2],line[3],line[4],line[5],line[3]*line[2],line[1]*line[4],line[1]**3,line[2]**3])
        
    thetaThirdDegree = []
    trainingSetMatrixTransposeThirdDegree = np.transpose(trainingSetMatrixThirdDegree)
    tempThirdDegree = np.matmul(trainingSetMatrixTransposeThirdDegree,trainingSetMatrixThirdDegree)
    tempThirdDegree = np.linalg.inv(tempThirdDegree)
    temp2ThirdDegree = np.matmul(tempThirdDegree,trainingSetMatrixTransposeThirdDegree)
    thetaThirdDegree = np.matmul(temp2ThirdDegree,trainingYMatrix)
    
    #print('Third order polynomial coefficients : ',thetaThirdDegree)
    
    #test for 3rd order polynomials
    print('\n\nThird order polynomial predictions')
    for line in testDataSet:
        val3 = thetaThirdDegree[0]+(thetaThirdDegree[1]*line[0])+(thetaThirdDegree[2]*line[1])+(thetaThirdDegree[3]*line[0]**2)+(thetaThirdDegree[4]*line[1]**2)+(thetaThirdDegree[5]*line[0]*line[1])+(thetaThirdDegree[6]*line[0]**2*line[1])+(thetaThirdDegree[7]*line[0]*line[1]**2)+(thetaThirdDegree[8]*line[0]**3)+(thetaThirdDegree[9]*line[1]**3)
        print('Actual value : ',line[2],' Predicted value : ',val3,' ,Error = ',val3-line[2])


    trainingSetMatrixFourthDegree = []
    for line in trainingSetMatrixThirdDegree:
        trainingSetMatrixFourthDegree.append([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[1]**4,line[2]**4,line[3]*line[4],line[6]*line[2],line[1]*line[7]])
        
    thetaFourthDegree = []
    trainingSetMatrixTransposeFourthDegree = np.transpose(trainingSetMatrixFourthDegree)
    tempFourthDegree = np.matmul(trainingSetMatrixTransposeFourthDegree,trainingSetMatrixFourthDegree)
    tempFourthDegree = np.linalg.pinv(tempFourthDegree)
    temp2FourthDegree = np.matmul(tempFourthDegree, trainingSetMatrixTransposeFourthDegree)
    thetaFourthDegree = np.matmul(temp2FourthDegree,trainingYMatrix)
    
    #print('Fourth Degree polynomial coefficients : ',thetaFourthDegree)
    
    #test for 4th order polynomials
    print('\n\nFourth order polynomial predictions')
    for line in testDataSet:
        val4 = thetaFourthDegree[0]+(thetaFourthDegree[1]*line[0])+(thetaFourthDegree[2]*line[1])+(thetaFourthDegree[3]*line[0]**2)+(thetaFourthDegree[4]*(line[1]**2))+(thetaFourthDegree[5]*line[0]*line[1])+(thetaFourthDegree[6]*(line[0]**2)*line[1])+(thetaFourthDegree[7]*line[0]*(line[1]**2))+(thetaFourthDegree[8]*line[0]**3)+(thetaFourthDegree[9]*line[1]**3)+(thetaFourthDegree[10]*line[0]**4)+(thetaFourthDegree[11]*line[1]**4)+(thetaFourthDegree[12]*line[0]**2*line[1]**2)+(thetaFourthDegree[13]*line[0]**3*line[1])+(thetaFourthDegree[14]*line[0]*line[1]**3)
        print('Actual value : ',line[2],' Predicted value : ',val4, ' ,Error = ',val4-line[2])

