from sys import argv
from math import sqrt
from random import choice
import time

begin = time.time()

def neighbour(training_data, test_row, k):
    euclidean_dist = list()
    for training_row in training_data:
        dist = 0.0
        for i in range(len(training_row)-1):
            dist += (training_row[i] - test_row[i])**2
        euclidean_dist.append([training_row, sqrt(dist)])
    euclidean_dist.sort(key=lambda row:row[1])
    neighbors = list()
    for i in range(int(k)):
        neighbors.append(euclidean_dist[i][0])
    return neighbors

py_file, train, test, k = argv

file_train = open(train, 'r')
file_test = open(test, 'r')

train_dataset = []
testing_dataset = []

for i in file_train:
    train_dataset.append([int(val) for val in i.split()])

for i in file_test:
    testing_dataset.append([int(val) for val in i.split()])

fv = []
for i in range(len(train_dataset[0])-1):
    column = [row[i] for row in train_dataset]
    mean = sum(column)/len(column)
    total = 0
    for val in column:
        total += abs((val - mean))**2
    
    fv.append({"mean": mean, "std": sqrt(total/len(column))})

train_size=len(train_dataset)
test_size=len(testing_dataset)

for i in range(train_size):
    for j in range(len(train_dataset[i])-1):
        train_dataset[i][j] = (train_dataset[i][j] - fv[j]["mean"])/fv[j]["std"]

for i in range(test_size):
    for j in range(len(testing_dataset[i])-1):
        testing_dataset[i][j] = (testing_dataset[i][j] - fv[j]["mean"])/fv[j]["std"]

acc = 0
for x in range(test_size):
    row = testing_dataset[x]
    vals = [row[-1] for row in neighbour(train_dataset, row, k)]
    counts = dict()

    for i in vals:
        counts[i] = counts.get(i, 0) + 1

    obj = [value for value in counts.values()]

    predicted = choice([key for key in counts if counts[key] == max(obj)])
    accuracy = 0

    vals = [row[-1] for row in neighbour(train_dataset, row, k)]

    counts = dict()

    for i in vals:
        counts[i] = counts.get(i, 0) + 1

    obj = [value for value in counts.values()]

    if obj.count(max(obj)) == 1:
        if (predicted ==row[-1]):
            accuracy = 1
        
    elif obj.count(max(obj)) > 1:
        if counts[predicted ] == max(obj):
            accuracy = 1/obj.count(max(obj))
        
    print("ID={0:5d}, predicted={1:3d}, actual={2:3d}, accuracy={3:5.2f}\n".format(x, predicted , row[-1], accuracy))
    acc += accuracy

print("Classification Accuracy= ",((acc/len(testing_dataset))*100),"%")
print("Code executed in %s minutes",((time.time() - begin)%60))