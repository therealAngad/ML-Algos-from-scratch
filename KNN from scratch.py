from math import sqrt

def euclidean_distance(row1,row2):
    dist=0.0
    for i in range(len(row1)-1):
        dist+=(row1[i]-row2[i])**2
    return sqrt(dist)


def get_neighbors(train, test_row, num_neighbors):
	distances = []
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row,dist))
	distances.sort(key=lambda list:list[1])
	neighbors = []
	for i in range(num_neighbors):
		neighbors.append(distances[i])
	return neighbors

def predict_classification(train,test_row,num_neighbors):
    neighbors = get_neighbors(train,test_row,num_neighbors)
    output_values=[row[-1] for row in neighbors]
    predict=max(output_values,key=output_values.count)
    return predict
    
'''
def nearest_neighbors(train_row,test_row,num_neighbours):
    diff=[]
    for row in train_row:
        distance=euclidean_distance(test_row,train_row)
        diff.append(distance)
    diff.sort()
    for i in num_neighbor:
        nearest_number.append(diff[i])
        return(nearest_number)
'''
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]


prediction = predict_classification(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))
'''
row0=dataset[0]
neighborfinal=nearest_neighbors(dataset,dataset[0],3)
for n in neighborfinal:
    print(n)
'''
