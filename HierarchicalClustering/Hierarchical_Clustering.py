"""
@author : Sundesh Raj
 UTA_ID : 1001633297
 CSE6363 Machine Learning
 Final Project
"""

import math
import os
#importing Python heap class to perform heap queue operations
#https://github.com/python/cpython/blob/3.7/Lib/heapq.py
import heapq
import time
import operator
from csv import reader
#suppress unwanted warnings
import warnings
warnings.filterwarnings("ignore")

class Hierarchical_Clustering:

    def __init__(self, unlabelledData, numOfClusters):
        self.input_file_name = unlabelledData
        self.k = numOfClusters
        self.dataset = None
        self.dataset_size = 0
        self.dimension = 0
        self.heap = []
        self.clusters = []
        self.gold_standard = {}
        
    def loadCSV(self, filename):
    	dataset = list()
    	with open(filename, 'r') as file:
    		csv_reader = reader(file)
    		for row in csv_reader:
    			if not row:
    				continue
    			dataset.append(row)
    	return dataset
    
    def convertStringToFloat(self, data, column):
        for line in data:
            line[column] = float(line[column])

    def initialize(self):
        # check file exist and if it's a file or dir
        if not os.path.isfile(self.input_file_name):
            self.quit("Input file doesn't exist or it's not a file")

        self.dataset, self.clusters, self.gold_standard = self.load_data(self.input_file_name)
        self.dataset_size = len(self.dataset)

        if self.dataset_size == 0:
            self.quit("Input file doesn't include any data")

        if self.k == 0:
            self.quit("k = 0, no cluster will be generated")

        if self.k > self.dataset_size:
            self.quit("k is larger than the number of existing clusters")

        self.dimension = len(self.dataset[0]["data"])

        if self.dimension == 0:
            self.quit("dimension for dataset cannot be zero")

    #calculate the euclidean distance between any 2 given points
    def euclidean_distance(self, data_point_one, data_point_two):
        size = len(data_point_one)
        result = 0.0
        for i in range(size):
            f1 = float(data_point_one[i])   # feature for data one
            f2 = float(data_point_two[i])   # feature for data two
            tmp = f1 - f2
            result += pow(tmp, 2)
        result = math.sqrt(result)
        return result

    #compute pair wise distance
    def compute_pairwise_distance(self, dataset):
        result = []
        dataset_size = len(dataset)
        for i in range(dataset_size-1):
            for j in range(i+1, dataset_size):
                dist = self.euclidean_distance(dataset[i]["data"], dataset[j]["data"])
                result.append( (dist, [dist, [[i], [j]]]) )

        return result
                
    def build_priority_queue(self, distance_list):
        heapq.heapify(distance_list)
        self.heap = distance_list
        return self.heap

    #calculate the centroid between 2 clusters
    def compute_centroid_two_clusters(self, current_clusters, data_points_index):
        size = len(data_points_index)
        dim = self.dimension
        centroid = [0.0]*dim
        for index in data_points_index:
            dim_data = current_clusters[str(index)]["centroid"]
            for i in range(dim):
                centroid[i] += float(dim_data[i])
        for i in range(dim):
            centroid[i] /= size
        return centroid

    #calculate the centroid of a cluster
    def compute_centroid(self, dataset, data_points_index):
        size = len(data_points_index)
        dim = self.dimension
        centroid = [0.0]*dim
        for idx in data_points_index:
            dim_data = dataset[idx]["data"]
            for i in range(dim):
                centroid[i] += float(dim_data[i])
        for i in range(dim):
            centroid[i] /= size
        return centroid

    def hierarchical_clustering(self):
        dataset = self.dataset
        current_clusters = self.clusters
        old_clusters = []
        heap = hClust.compute_pairwise_distance(dataset)
        heap = hClust.build_priority_queue(heap)

        while len(current_clusters) > self.k:
            dist, min_item = heapq.heappop(heap)
            # pair_dist = min_item[0]
            pair_data = min_item[1]

            # judge if include old cluster
            if not self.valid_heap_node(min_item, old_clusters):
                continue

            new_cluster = {}
            new_cluster_elements = sum(pair_data, [])
            new_cluster_cendroid = self.compute_centroid(dataset, new_cluster_elements)
            sorted(new_cluster_elements)
            new_cluster.setdefault("centroid", new_cluster_cendroid)
            new_cluster.setdefault("elements", new_cluster_elements)
            for pair_item in pair_data:
                old_clusters.append(pair_item)
                del current_clusters[str(pair_item)]
            self.add_heap_entry(heap, new_cluster, current_clusters)
            current_clusters[str(new_cluster_elements)] = new_cluster
        sorted(current_clusters)
        time.sleep(2)
        return current_clusters
            
    #validate the heap node
    def valid_heap_node(self, heap_node, old_clusters):
        pair_data = heap_node[1]
        for old_cluster in old_clusters:
            if old_cluster in pair_data:
                return False
        return True
      
    #add new heap item
    def add_heap_entry(self, heap, new_cluster, current_clusters):
        for ex_cluster in current_clusters.values():
            new_heap_entry = []
            dist = self.euclidean_distance(ex_cluster["centroid"], new_cluster["centroid"])
            new_heap_entry.append(dist)
            new_heap_entry.append([new_cluster["elements"], ex_cluster["elements"]])
            heapq.heappush(heap, (dist, new_heap_entry))

    #load the data set
    def load_data(self, input_file_name):
        input_file = open(input_file_name, 'rU')
        dataset = []
        clusters = {}
        gold_standard = {}
        id = 0
        for line in input_file:
            line = line.strip('\n')
            row = str(line)
            row = row.split(",")
            seeds_class = row[-1]

            data = {}
            data.setdefault("id", id)
            data.setdefault("data", row[:-1])
            data.setdefault("class", row[-1])
            dataset.append(data)

            #create cluster elements
            clusters_key = str([id])
            clusters.setdefault(clusters_key, {})
            clusters[clusters_key].setdefault("centroid", row[:-1])
            clusters[clusters_key].setdefault("elements", [id])

            gold_standard.setdefault(seeds_class, [])
            gold_standard[seeds_class].append(id)

            id += 1
        return dataset, clusters, gold_standard

    def quit(self, err_desc):
        raise SystemExit('\n'+ "PROGRAM EXIT: " + err_desc + ', please check your input' + '\n')
    
    #calcuate the distance between given 2 points
    def calculateDistance(self, instance1, instance2, length):    
        dis = 0
        for x in range(length):
            dis += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(dis)
    
    #perform the class prediction
    def predictClass(self, neighbours):    
        classes = {}
        for neighbour in neighbours:
            currClass = neighbour[-1]
            if currClass in classes:
                classes[currClass] += 1
            else:
                classes[currClass] = 1
        sortedClass = sorted(classes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClass[0][0]
    
    #get the nearest neighbours for the input data
    def findNeighbours(self, training, testInstance, k):
        distances = []
        length = len(testInstance)
        for instance in training:
            dist = hClust.calculateDistance(testInstance, instance, length)
            distances.append((instance, dist))
        distances.sort(key=operator.itemgetter(1))
        neighbours = []
        for instance in range(k):
            neighbours.append(distances[instance][0])
        return neighbours
    
    def knnClassifier(self, X, test, k):
        neighbours = hClust.findNeighbours(X, test, k)
        prediction = hClust.predictClass(neighbours)
        return prediction
    
    #add labels to the dataset based on the clusters formed
    def addLabels(self, current_clusters, dataSet):
        clusters = current_clusters.values()
        count = 0
        indexes = list()
        cluster1 = list()
        cluster2 = list()
        cluster3 = list()
        for clust in clusters:
            for c in clust["elements"]:
                indexes.append(c)
            count += 1
            if count == 1:
                cluster1 = indexes
                for i in cluster1:
                    dataSet[i][7] = 1.0
                indexes.clear()
            if count == 2:
                cluster2 = indexes
                for i in cluster2:
                    dataSet[i][7] = 2.0
                indexes.clear()
            if count == 3:
                cluster3 = indexes
                for i in cluster3:
                    dataSet[i][7] = 3.0
                indexes.clear()

if __name__ == '__main__':

    unlabelledData = "seeds.csv"      # input data
    numOfClusters = 3    #number of clusters, e.g. 3

    hClust = Hierarchical_Clustering(unlabelledData, numOfClusters)
    hClust.initialize()
    #duplicate training data to write the new labels
    datas = hClust.loadCSV("seedsDuplicate.csv")
    for n in range(len(datas[0])):
        hClust.convertStringToFloat(datas, n)
    testData = hClust.loadCSV("testData.csv")
    for m in range(len(testData[0])):
        hClust.convertStringToFloat(testData, m)
    current_clusters = hClust.hierarchical_clustering()
    hClust.addLabels(current_clusters, datas)
    print("===============================================================")
    print("Hierachical Clustering Of the Seeds data set (UCI Seeds Dataset)")
    print("===============================================================")
    print("The clusters created from",unlabelledData,"are :\n")
    print("The below clusters show the row index of the data belonging to different clusters :\n")
    pClust = current_clusters.values()
    for c in pClust:
        print(c,'\n')
    print("===============================================================")
    print("Predictions for the test data : ")
    print("===============================================================")
    time.sleep(2)
    for item in testData:
        print('Predicted class for',item,' :' , + hClust.knnClassifier(datas, item, 3))