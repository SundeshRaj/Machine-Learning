============================SXR3297 README TXT file for HW1============================

Name : Sundesh Raj
Course: CSE-6363-001 (Machine Learning)
UTAID : 1001633297

The zip file "Howework1_sxr3297.zip" consists of 2 sub folders, "Written" and "Programming"

Written:
--------

1. The written folder contains "Homework1_sxr3297.pdf" file which contains solutions to the questions 1a, 1b, 1c, 2a, 2c, 3a, 3c and 3d
2. All the written solutions are in this pdf

Programming:
------------

1. The "Programming" folder contains 2 sub folders - "KNN" and "Naive Bayes"
2. The "KNN" folder contains - "2bknnclassifier.py", "2bdata.csv", "2cknnclassifier.py" and "2cdata.csv"
3. The "2bknnclassifier.py" has the "2bdata.csv" file as input file.
	-This python file is for the data including the age parameter
	-To run this execute - python 2bknnclassifier.py 2bdata.csv <height> <weight> <age> <k-value>
	-Example "python 2bknnclassifier.py 2bdata.csv 155 40 35 3" in this order
	-We can make changes to the 2bdata.csv file if any other training data needs to be added
4. The "2cknnclassifier.py" has the "2cdata.csv" file as input file.
	-This python file is for the data excluding the age parameter
	-To run this execute - python 2bknnclassifier.py 2bdata.csv <height> <weight> <k-value>
	-Example "python 2bknnclassifier.py 2bdata.csv 155 40 3" in this order
	-We can make changes to the 2bdata.csv file if any other training data needs to be added
5. The "Naive Bayes" folder contains 2 python files - "3bnaivebayes.py" and "3cnaivebayes.py"
	-The "3bnaivebayes" is with the age data included.
	-The training data is encoded within the python file and can be changed at lines 77 to 80
	-The input parameters can also be changed at lines 72 to 74
	-To run this file execute "python 3bnaivebayes.py"
	
	-The "3cnaivebayes.py" is without the age parameter
	-The training data is encoded within the python file and can be changed at lines 56 to 58
	-The input parameters can also be changed at lines 52 to 53
	-To run this file execute "python 3cnaivebayes.py"
	
6. All the programming files are tested with python 2.4 and are compatible and executable in OMEGA


External References and Citations:
----------------------------------
1.https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
2.https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Testing
3.https://stackoverflow.com/questions/16670658/python-variance-of-a-list-of-defined-numbers
4.https://www.tutorialspoint.com/python/number_exp.htm
5.https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
6.https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
7.https://www.e-education.psu.edu/geog485/node/141
8.https://machinelearningmastery.com/naive-bayes-for-machine-learning/
9.https://www.python-course.eu/k_nearest_neighbor_classifier.php
10.https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/


============================================================================================================
=============================================END OF FILE====================================================
============================================================================================================