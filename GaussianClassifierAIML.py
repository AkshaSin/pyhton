#learning what gaussian classifiers are
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

iris= load_iris()
df=pd.DataFrame(iris['data'])
print(df)
print(iris['target_names'])
print ("Features: ", iris.feature_names)
print ("Target: ", iris.target_names)

X=pd.DataFrame(iris['data'])
y=iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.40,random_state=109)

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)
print(y_pred)

# Model Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

