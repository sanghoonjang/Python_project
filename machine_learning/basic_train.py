
# Basic Train

""" iris.csv
SepalLength,SepalWidth,PetalLength,PetalWidth,Name
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
....
"""

import pandas as pd
from sklearn import svm, metrics, cross_validation

csv = pd.read_csv('iris.csv')

csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]

train_data, test_data, train_label, test_label = \
  cross_validation.train_test_split(csv_data, csv_label)

clf = svm.CVS()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("Percentage :", ac_score)
