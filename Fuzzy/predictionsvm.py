import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("diabetes.csv")
print(dataset.describe())
print(dataset['Outcome'].value_counts())
# separating the dataset into x and y axis
X = dataset.drop(columns ='Outcome',axis =1)
Y = dataset['Outcome']
# StandardScaler for converting the values to 0 to 1
scaler = StandardScaler()
scaler.fit(X)
standard = scaler.transform(X)
X = standard
print(X)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify =Y,random_state=2)
# fitting the xtrain to classifier as svm
classifier = svm.SVC(kernel = "linear")
classifier.fit(X_train,Y_train)
# to calculate the accuracy score of both xtrain and x_test
dataset_prediction = classifier.predict(X_train)
Accuracy_train=accuracy_score(dataset_prediction,Y_train)
print(Accuracy_train)
dataset_prediction1 = classifier.predict(X_test)
Accuracy_test=accuracy_score(dataset_prediction1,Y_test)
print(Accuracy_test)
# making predictive system with sample input
input_data = (8,183,64,0,0,23.3,0.672,32)
# to convert into numpy array
input_data_array = np.asarray(input_data)
# to reshape into perform dataset_prediction
input_data_reshape= input_data_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshape)
prediction = classifier.predict(std_data)
print(prediction)
