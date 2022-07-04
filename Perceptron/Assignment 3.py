import random 
import matplotlib.pyplot as ax 
import numpy as np
import sys

ax.ion()
data_points = [[random.randint(0,1000),random.randint(0,1000)] for i in range(20) ]
points = []

for i in data_points:
    val = i[1]-i[0]+30
    if val > 0:
        points.append(1)
    else:
        points.append(-1)

data_points = np.array(data_points)

b, w1, w2 = random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)
n, epoch = 0.0001, 0

while(True):
    epoch = epoch + 1
    error = 0
    for i in range(20):
        total = b + (w1 * data_points[i][0]) + (w2 * data_points[i][1])
        if total>0:
            output=1
        else:
            output=-1    
        if output != points[i]:
            w1 = w1 + n * points[i]- output * data_points[i][0]
            w2 = w2 + n * points[i]- output * data_points[i][1]
            b = b + n * points[i] - output * b
            error = error + 1
    y = data_points-30        

    for i in range(len(data_points)):
        if(points[i] == -1):
            ax.scatter(data_points[i][0],data_points[i][1],color='k',facecolors='none', edgecolors='k')
        else:
            ax.scatter(data_points[i][0],data_points[i][1],facecolors='k', edgecolors='k')

    x_train = np.linspace(0,1000,100)
    y_train = (-w1*x_train - b)/float(w2)

    ax.plot(data_points,y,'-g')
    ax.plot(x_train,y_train,'-y',label="Perceptron training line")
    ax.legend()
    ax.show()  
    print("Epoch - ",epoch," Misclassified points - ",error)

    if (error==0):
        print("Perceptron trained successfully!")
        print("Press 1 to terminate the program: ")
        x=int(input())
        if x==1:
            sys.exit(0)
    else:
        ax.pause(2)
        ax.clf()