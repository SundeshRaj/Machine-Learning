"""
@author: sundesh raj
UTA_ID : 1001633297
"""

from csv import reader

def loadCSV(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

#method to find unique values with respect to each feature
def uniqueValues(rows, col):
    return set([row[col] for row in rows])

def class_counts(rows):
    #keeps count of the number of data with respect to each class
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)

class BuildTree:

    def __init__(self, column, value):
        self.column = column
        self.value = value

	#comparing feature values to the condition check
    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))
        
#split dataset with respect to the class and compare with the condition and assign to respective true/false rows
def splitDataset(rows, condition):
    true_rows, false_rows = [], []
    for row in rows:
        if condition.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

#calculate the GINI impurity for the list of data rows
def giniImpurityCheck(rows):
    counts = class_counts(rows)
    impurity = 1
    for k in counts:
        k_probability = counts[k] / float(len(rows))
        impurity -= k_probability**2
    return impurity

#calculate the information gain
def informationGain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * giniImpurityCheck(left) - (1 - p) * giniImpurityCheck(right)

#find the best split and the root node based on the maximum information gain and add to the tree
def chooseBestNode(rows):
    winningGain = 0
    bestNodeChosen = None
    current_uncertainty = giniImpurityCheck(rows)
    num_of_features = len(rows[0]) - 1  # number of columns

    for col in range(num_of_features):  # for each feature

        values = set([row[col] for row in rows])  # unique values in the column

        for val in values:  # for each value

            condition = BuildTree(col, val)

            true_rows, false_rows = splitDataset(rows, condition)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

			#calculate the information gain
            gain = informationGain(true_rows, false_rows, current_uncertainty)

			#assign maximum gain and the best chosen condition
            if gain >= winningGain:
                winningGain, bestNodeChosen = gain, condition

    return winningGain, bestNodeChosen

#the leaf node class
class LeafNode:

    def __init__(self, rows):
        self.predictions = class_counts(rows)
        
#the decision node class checks for the proper condition to assign the next successive node in the tree
class Decision_Node:

    def __init__(self,
                 condition,
                 true_branch,
                 false_branch):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

#the build tree method to find the decision node and build the tree recursively        
def build_tree(rows):

    gain, condition = chooseBestNode(rows)

	#return leaf node if no other gain is found
    if gain == 0:
        return LeafNode(rows)

    true_rows, false_rows = splitDataset(rows, condition)

    # Recursively build the true branch.
    true_branch = build_tree(true_rows)

    # Recursively build the false branch.
    false_branch = build_tree(false_rows)

    #return the decision tree based on the true and false conditions checked
    return Decision_Node(condition, true_branch, false_branch)

#a display class to view the decision tree constructed
def display_Decision_Tree(node, spacing=""):

    if isinstance(node, LeafNode):
        print (spacing + "Predict", node.predictions)
        return

    # Print the condition at this node
    print (spacing + str(node.condition))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    display_Decision_Tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    display_Decision_Tree(node.false_branch, spacing + "  ")
    
#printing the leaf nodes and prediction values
def print_leaf_nodes(counts):
    total = sum(counts.values()) * 1.0
    probability = {}
    for k in counts.keys():
        probability[k] = str(int(counts[k] / total * 100)) + "%"
    return probability

#classify the nodes based on the true or false condition
def classify(row, node):

    if isinstance(node, LeafNode):
        return node.predictions
		
    if node.condition.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

#for mathematical convenience the classs column is moved to the last column and we have dropped the Odour feature set
trainingDataFile = "MushroomTrain.csv"
trainingDataSet = loadCSV(trainingDataFile)
testDataFile = "MushroomTest.csv"
testDataSet = loadCSV(testDataFile)

#assign column headers for the data set
header = ["cap-shape", "cap-surface", "cap-color","bruises","label"]

#build the decision tree from the training data set
print ("================================")
print ("= Displaying the Decision Tree =")
print ("================================")
dTree = build_tree(trainingDataSet)
display_Decision_Tree(dTree)

#iteratie through the data set and print the results for the test Dataset
print ("\n")
print ("==================================")
print ("Predictions for Training Dataset!!")
print ("==================================")
for row in trainingDataSet:
	print ("Actual Value: %s. Predicted Value: %s" %(row[-1], print_leaf_nodes(classify(row, dTree))))

#iteratie through the data set and print the results for the test Dataset
print ("\n")
print ("==============================")
print ("Predictions for Test Dataset!!")
print ("==============================")
for row in testDataSet:
    print ("Actual Value: %s. Predicted Value: %s" %(row[-1], print_leaf_nodes(classify(row, dTree))))