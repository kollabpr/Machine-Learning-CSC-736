import numpy as np
import matplotlib.pyplot as ax
import csv
from sklearn.model_selection import train_test_split

vector = []
epoch = 0
for i in range(4):        
    a =[]
    for j in range(4):     
        if i==j:
            a.append(float(0.9))
        else:
            a.append(float(0.1))
    vector.append(a)

learning_rate = 0.01
correctly_classified = 0
wji, wkj = [], [] #weights
dj, dk=[], [] #delta
bj, bk=[], [] #bias
yk=[] # hidden output layer
yj=[] # hidden input layer

hidden_nodes=int(input("Please enter the number of hidden nodes: "))

def feed_forward_nn(data):
    yj, yk = [], []

    for j in range(5):
        total = 0
        for i in range(64):
            total += data[i]*wji[i][j]
        total = total + bj[j]   
        yj.append(1 / (1 + np.exp(-total)))   
    
    for i in range(4):
        total = 0
        for j in range(5):
            total += yj[j]*wkj[j][i]
        total = total + bk[i]    
        yk.append(1 / (1 + np.exp(-total)))

    return yj,yk
    
def back_propagation(data,trained_outputs, yj, yk):

    for i in range(len(trained_outputs)):
        dk[i] = ( yk[i] * (1 - yk[i]) * (trained_outputs[i] - yk[i]))
    
    for i in range(len(yj)):
        sum=0
        for j in range(len(dk)):
            sum = sum + dk[j] * wkj[i][j]
        dj[i] =  yj[i]*(1-yj[i])*sum
    
    for j in range(5):
        bj[j] =  bj[j] + learning_rate*bj[j]*dj[j]
        for k in range(4):
            wkj[j][k] = wkj[j][k] + learning_rate*dk[k]*yj[j]
            bk[k] = bk[k] + learning_rate*bk[k]*dk[k]
    
    for i in range(64):
        for j in range(5):
            wji[i][j] = wji[i][j]+ learning_rate * dj[j]*data[i]
         
def mse_calculation(data,actual_output):

    result=[]
    sum_square= 0
    for i in range(len(data)):
        yj,yk = feed_forward_nn(data[i])
        result.append(yk)
    
    for i in range(len(result)):
        for j in range(4):
            sum_square = sum_square + (actual_output[i][j] - result[i][j])**2
    return (sum_square / 2 ) 

train,test=[], []
train_output, test_output=[], []

with open('optdigits-3.tra') as file1:
    training_file = csv.reader(file1, delimiter=',')
    for row in training_file:
        rows=[]
        for i in range(64):
            rows.append( (int(row[i]))/16)
        output = int(row[64])
        train_output.append(vector[output])
        train.append(rows)

with open('optdigits-3.tes') as file2:
    testing_file = csv.reader(file2, delimiter=',')
    for row in testing_file:
        rows=[]
        for i in range(64):
            rows.append( (int(row[i]))/16)
        output = int(row[64])
        test_output.append(vector[output])
        test.append(rows)

inputs_training,inputs_testing, outputs_training,  outputs_testing = train_test_split(train, train_output, test_size=0.20, random_state=32)

for x in range(64*hidden_nodes):
    wji.append(round(np.random.uniform(-1,1),3))

for x in range(hidden_nodes*4):
    wkj.append(round(np.random.uniform(-1,1),3))

wji= np.reshape(wji,(64,hidden_nodes)).tolist()    
wkj= np.reshape(wkj,(hidden_nodes,4)).tolist()

for x in range(hidden_nodes):
    bj.append(round(np.random.uniform(-1,1),3))

for x in range(4):
    bk.append(round(np.random.uniform(-1,1),3)) 

dj = [0.0]*hidden_nodes
dk = [0.0]*4
yk = [0.0]*4
model_train, model_test, num_epochs, result= [], [], [], []

while(epoch<20000):
    ax.clf()

    for i in range(len(inputs_training)):
        yj,yk = feed_forward_nn(inputs_training[i])
        back_propagation(inputs_training[i], outputs_training[i], yj, yk)

    if epoch %10 ==0:
        train_val =mse_calculation(inputs_training,outputs_training)
        test_val = mse_calculation(inputs_testing,outputs_testing)
       
        model_train.append( train_val) 
        model_test.append(test_val)
        
        print("epoch - ", epoch,"MSE - ",train_val)
        
        num_epochs.append(epoch)
        ax.plot(num_epochs, model_train,  label = 'Training Data' )
        ax.plot(num_epochs, model_test,   label = 'Testing Data' )
        ax.legend()
        ax.xlabel( "No. of epochs" )
        ax.ylabel( "MSE" )
        ax.draw( )
        ax.pause(0.01)
    epoch += 1   
    if test_val<=2:
        break

for i in range(len(test)):
    yj,yk = feed_forward_nn(test[i])
    result.append(yk)

for i in range(len(result)):
    if( test_output[i].index(max(test_output[i])) == result[i].index(max(result[i]))):
        correctly_classified += 1

print("Accuracy : ",(correctly_classified/len(result) *100)," obtained with ",hidden_nodes," nodes!")
x=input("Press any button to terminate the program")