import random as rand
import matplotlib.pyplot as ax 
import numpy

ax.ion()
x=[]
for val in range(20):
    x.append(rand.randint(0,500))
x = numpy.array(x)
Y = []

for val in x:
    y = 2*val+3
    Y.append(y + (y * 0.1*rand.choice([1,-1])))

bias, weight, learning_rate = rand.uniform(0,1), rand.uniform(0,1), 0.000001

epoch=1
while epoch<=50:
    linear_regressor_model=[]
    
    for val in range(20):
        linear_regressor_model.append(weight*x[val]+bias)
    
    bias_error = 0
    weight_error = 0
    mean_squared_error = 0
    
    for val in range(20):
        temp = Y[val]-linear_regressor_model[val]
        bias_error += temp
        weight_error += temp*x[val]
        mean_squared_error = temp**2

    bias = bias + learning_rate * (bias_error/20)
    weight = weight + learning_rate * (weight_error/20)
    
    ax.scatter(x,Y,facecolors='k')
    ax.plot(x,2*x+3,'-g',label='y=2x+3')
    ax.plot(x,linear_regressor_model,'-y',label='Linear Regressor Training Line')
    ax.legend()
    ax.show()   
    ax.pause(.001)
    ax.clf()
    print("Epoch - ",epoch," Mean Squared Error : ",mean_squared_error/20)
    epoch = epoch + 1