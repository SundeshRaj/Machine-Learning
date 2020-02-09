============================SXR3297 README TXT file for Final Project============================

Name : Sundesh Raj
Course: CSE-6363-001 (Machine Learning)
UTAID : 1001633297

The zip file "SXR3297_FinalProject.zip" consists of sub folder, "HierarchicalClustering" and 2 additional files

-ZIP File contents-
/HierarchicalClustering
/README.txt
/SXR3297_FinalProject_Report.docx

External References and Citation:
---------------------------------
https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
https://medium.com/datadriveninvestor/unsupervised-learning-with-python-k-means-and-hierarchical-clustering-f36ceeec919c
https://github.com/ZwEin27/Hierarchical-Clustering
https://en.wikipedia.org/wiki/Complete-linkage_clustering
https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/
https://pythonprogramming.net/hierarchical-clustering-machine-learning-python-scikit-learn/
https://datascience.stackexchange.com/questions/26206/calculate-distance-between-each-data-point-of-a-cluster-to-their-respective-clus
https://github.com/benjaminwilson/python-hierarchical-clustering-exercises/blob/master/solutions/solution_10_hierarchical_clustering_grain.ipynb
https://www.datacamp.com/community/tutorials/hierarchical-clustering-R
https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
https://www.python-course.eu/k_nearest_neighbor_classifier.php
https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file

HierarchicalClustering:
-----------------------
-The folder contains the 2 python files "Hierarchical_Clustering.py", "heapq.py"
-The folder also contains 3 csv files "seeds.csv", "seedsDuplicate.csv" and "testData.csv"

"Hierarchical_Clustering.py":
-----------------------------
-Main functions:
	-loadCSV(), loads the duplicate CSV file
	-initialize(), initializes all the datasets, does valdidation on the input given
	-euclidean_distance(self, data_point_one, data_point_two), calculate the euclidean distance between given points
	-compute_pairwise_distance(self, dataset), calculate the distance between any 2 given clusters
	-build_priority_queue(self, distance_list), implement a priority queue based on the distance between the clusters
	-compute_centroid_two_clusters(self, current_clusters, data_points_index), calculating the centroid distance between any 2 clusters
	-compute_centroid(self, dataset, data_points_index), calculating the centroid of a particular cluster
	-hierarchical_clustering(self), the main function which performs the clustering, building the priority queue
	-addLabels(self, current_clusters, dataSet), add labels to the unlabelled dataset based on the cluster ID's
	
	KNN functions:
	-findNeighbours(self, training, testInstance, k)
	-predictClass(self, neighbours)
	-calculateDistance(self, instance1, instance2, length)
	-knnClassifier(self, X, test, k)
	
Execution Environment:
----------------------
Anaconda Spyder IDE with Python version 3.6.5
	
Code Structure:
---------------
	-The main function imports the data sets required. Initially the unlabelled data and the duplicate data are loaded
	-The unlabelled data is passed as the parameter into the hierarchical_clustering(self) method which returns the clusters
	-Based on the clusters the addLabels() method adds respective labels to the datapoints based on the cluster
	-Finally the labelled dataset and the test dataset is passed as parameters to the knnClassifier(self, X, test, k) method
	 which returns the prediction of the test data based on the nearest neighbour classifier
	-The output is printed in the console
	
Code Execution:
---------------
-Make sure the python files and the csv files are in the same folder
-The code can be run on any machine supporting Python 3.6.5
-I have executed the code on the Anaconda Spyder IDE
-On command line, the execution call is "python Hierarchical_Clustering.py"