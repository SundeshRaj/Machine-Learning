============================SXR3297 README TXT file for PROJECT1============================

Name : Sundesh Raj
Course: CSE-6363-001 (Machine Learning)
UTAID : 1001633297

The zip file "Project1_sxr3297.zip" consists of 2 sub folders, "Written" and "Programming"

External References and Citations:
----------------------------------
1.https://machinelearningmastery.com/implement-logistic-regression-stochastic-gradient-descent-scratch-python/
2.http://kt.ijs.si/theses/phd_aleksandar_peckov.pdf
3.https://www.originlab.com/doc/Origin-Help/PR-Algorithm
4.https://algs4.cs.princeton.edu/14analysis/PolynomialRegression.java.html
5.https://www.codeproject.com/Articles/566326/Multi-Linear-Regression-in-Java
6.https://glowingpython.blogspot.com/2012/01/how-to-plot-two-variable-functions-with.html
7.http://www.eas.uccs.edu/~mwickert/ece1010/lecture_notes/1010n6a.PDF
8.http://www.engineering.uco.edu/~aaitmoussa/Courses/ENGR3703/Chapter5/ch5.pdf
9.https://www.geeksforgeeks.org/program-for-rank-of-matrix/
10.http://www.statsoft.com/textbook/multiple-regression
11.https://stackoverflow.com/questions/37352098/ploting-a-polynomial-using-matplotlib-and-coeffiecients?rq=1
12.https://people.revoledu.com/kardi/tutorial/LDA/Numerical%20Example.html
13.http://reliawiki.org/index.php/Multiple_Linear_Regression_Analysis
14.https://stackoverflow.com/questions/40034993/how-to-get-element-wise-matrix-multiplication-hadamard-product-in-numpy
15.http://polynomialregression.drque.net/math.html

Written:
--------

The written section contains a PDF with the conclusions of all 3 questions in the Project.
There are conclusions and discussions for questions 1c, 2c and 3c


Programming:
---------------------------------------------------------------------------
Note: The python programs use numpy package and are not compatible in OMEGA
---------------------------------------------------------------------------
1. The "Programming" folder contains 3 sub folders - "PolynomialCurveFitting", "LogisticRegression" and "LinearDiscriminativeAnalysis"
2. The "PolynomialCurveFitting" folder contains "PolynomialCurveFitting.py", "data.csv" and "testData.csv" files
	- The "PolynomialCurveFitting.py" file takes both the csv files as input.
	- Any modifications to the training and the test data set can be made to these input csv files
	- Run the python file and it outputs the predictions and errors for the test data set
	- The THETA values for different order polynomials are stored in "thetaFirstDegree","thetaSecondDegree",""thetaThirdDegree" and "thetaFourthDegree"
	  variables respectively
	  
3. The "LogisticRegression" folder contains "LogisticRegression.py" file
	- The training and the test data are both hard coded in the python file
	- If any changes needs to be done to the training and the test data set it can be done to the code at lines "66" and "77" respectively
	- Running the python file will output the co-efficients and predictions for the class M or W

4. The "LinearDiscriminativeAnalysis" folder contains "LinearDiscriminativeAnalysis.py", "data.csv" and the "testData.csv"
	- The "LinearDiscriminativeAnalysis.py" file takes both the csv files as input
	- Any modifications to the training and the test data set can be made to these input csv files
	- Run the python file and it outputs the predictions and the generated sample data with respect to Men and Women
	- The graph for training data Height vs Weights and random generated data Height vs Weights is plotted
	- The number of sample data required can be changed at line "167" and "168" respectively for Men and Women