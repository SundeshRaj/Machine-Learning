"""
@author: sundesh raj
UTA_ID : 1001633297
"""

# importing some basic libraries
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

#the SVM Class
class SupportVectorMachine():
    def __init__(self,visualize=True):
        self.visualize = visualize
        self.colors = {1:'r',-1:'b'}
        #graph visualization
        if self.visualize:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    
    #Fitting the data to the SVM
    def fit(self,data):
        self.data = data
        # dictionary for holding values in the form ||w||:[w,b]
        w_dict = {}
        
        transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]
        
        dataset = np.array([])
        for y in self.data:
            dataset = np.append(dataset,self.data[y])
                    
        self.max_value = max(dataset)         
        self.min_value = min(dataset)
        dataset = None
        
        #with smaller steps our margins and db will be more precise
        step_sizes = [self.max_value * 0.1,
                      self.max_value * 0.01,
                      #point of expense
                      self.max_value * 0.001,]
        
        
        b_step_size = 5
        
        l_optimum = self.max_value*10
        
        #making step smaller and smaller to get precise value
        for step in step_sizes:
            w = np.array([l_optimum,l_optimum])#start with bigger random w value
            
            #we can do this because convex
            optimum = False
            while not optimum:
                for b in np.arange(-1*self.max_value*b_step_size,
                                   self.max_value*b_step_size,
                                   step*b_step_size):
                    for t in transforms:
                        w_t = w*t
                        opt = True
                        
                        for i in self.data:
                            for x in self.data[i]:
                                y=i
                                #yi(w.x)+b>=1
                                if not y*(np.dot(w_t,x)+b)>=1:
                                    opt=False
                        if opt:
                            w_dict[np.linalg.norm(w_t)]=[w_t,b]
                
                #optimising the w value
                if w[0]<0:
                    optimum=True
                    print("Optimized a step!!")
                else:
                    w = w-step
                    
            # sorting ||w|| to put the smallest ||w|| at poition 0 
            w_sorted = sorted([n for n in w_dict])
            #optimal values of w,b
            optimum_values = w_dict[w_sorted[0]]

            self.w=optimum_values[0]
            self.b=optimum_values[1]
            
            #iterate with new l_optimum values for w
            l_optimum = optimum_values[0][0]+step*2
    
    #graph plotting and drawing the gutter margins and optimal margin
    def draw(self):
        [[self.ax.scatter(x[0],x[1],s=100,c=self.colors[i]) for x in data_dict[i]] for i in data_dict]
        
        def hyperplane(x,w,b,v):
            return (-w[0]*x-b+v)/w[1]
       
        hyperX_Min= self.min_value*0.9
        hyperX_Max = self.max_value*1.1
        
        #positive gutter hyperplane
        #(w.x+b)>=1
        positivePlane1 = hyperplane(hyperX_Min,self.w,self.b,1)
        positivePlane2 = hyperplane(hyperX_Max,self.w,self.b,1)
        self.ax.plot([hyperX_Min,hyperX_Max],[positivePlane1,positivePlane2],'k')
        
        #negative gutter hyperplane
        #(w.x+b)<=-1
        negativePlane1 = hyperplane(hyperX_Min,self.w,self.b,-1)
        negativePlane2 = hyperplane(hyperX_Max,self.w,self.b,-1)
        self.ax.plot([hyperX_Min,hyperX_Max],[negativePlane1,negativePlane2],'k')
        
        #marginal vector hyperplane
        #(w.x+b) = 0
        marginalPlane1 = hyperplane(hyperX_Min,self.w,self.b,0)
        marginalPlane2 = hyperplane(hyperX_Max,self.w,self.b,0)
        self.ax.plot([hyperX_Min,hyperX_Max],[marginalPlane1,marginalPlane2],'y--')
        
        print('The value for w = ',self.w)
        print('The value for b = ',self.b)
        
#defining input data
data_dict = {-1:np.array([[1,2],[2,1],[1,3]]),1:np.array([[2,3],[3,4],[4,4]])}

svm = SupportVectorMachine()#call SVM class to initialize the object
svm.fit(data=data_dict)#fit the input data to the SVM model
svm.draw()#visualize the results