

'''
def mean(values):
	return sum(values) / float(len(values))
 
# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])
 
# calculate mean and variance
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
print(mean_x)
'''
from math import sqrt
def mean(values):
    return sum(values) / float(len(values))

def variance(values,mean):
    return sum((x-mean)**2 for x in values)

def covariance(x,mean_x,y,mean_y):
    total=0
    for i in range(len(x)):
        total+=( (x[i]-mean_x)*(y[i]-mean_y))
    return total

def coefficients(dataset):
    x=[row[0] for row in dataset]
    y=[row[1] for row in dataset]
    mean_x,mean_y=mean(x),mean(y)
    variance_x,variance_y=variance(x,mean_x),variance(y,mean_y)
    covariance_ans=covariance(x,mean_x,y,mean_y)
    b1=covariance_ans/variance_x
    b0=mean_y-b1*mean_x
    return b0,b1;
'''
def evaluate_algorithm(values,algorithm):
    test=[]
    for row in values:
        row_copy=row
        row_copy[-1]=None
        test.append(row_copy)
    pred=algorithm(values, test)
    print(pred)
    actual=[[row[-1] for row in values]]
    rmse=rmse_metrics(actual, pred)
    return rmse
    '''
def evaluate_algorithm(dataset, algorithm):
    test_set = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
    predicted = algorithm(dataset, test_set)
    print(predicted)
    actual = [row[-1] for row in dataset]
    rmse = rmse_metric(actual, predicted)
    return rmse

def simple_linear_regression(train,test):
    b0,b1=coefficients(train)
    pred=[]
    for row in train:
        y=b0+b1*row[0]
        pred.append(y)
    return pred

def rmse_metric(actual,pred):
   sum_error = 0.0
   for i in range(len(actual)):
       prediction_error = pred[i] - actual[i]
       sum_error += (prediction_error ** 2)
   mean_error = sum_error / float(len(actual))
   return sqrt(mean_error)

    
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
rmse=evaluate_algorithm(dataset,simple_linear_regression)
print(rmse)
