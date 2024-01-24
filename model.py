import pandas
import numpy as np
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pandas.read_csv('Dataset.csv') #reading the csv file
y = df['Type'] #extracting the target variable to y
X = df.drop(['Type'],axis = 1) #removing the target variable from the training dataset

X_train, X_test, y_train, y_test =  train_test_split(X,y,test_size = 0.20) 
#splitting the training and testing data approx 80% of data is training data while 20% data will be used for testing
X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)
#converting each data records into numpy arrays for easy manipulation
print("Creating model")

#implementing random forest model
rf = RandomForestClassifier( n_estimators = 70,max_features = 'sqrt',max_depth = 20,min_samples_split = 4,min_samples_leaf = 1,bootstrap = False) 
rf.fit(X_train,y_train)
#fitting the traing data into the model

#exporting the model
filename = "model"
pickle.dump(rf, open(filename,'wb'))
print("Model Created Successfully")