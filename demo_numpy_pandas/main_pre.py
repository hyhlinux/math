import numpy as np
from sklearn.svm import SVC



X = np.array([[1],[2],[3]])
Y = np.array([1,2,3])
x_first = np.array([[1],[2]])
x_second = np.array([[2],[3]])
y_first = np.array([1,2])
y_second = np.array([2,3])
clf = SVC()
clf.fit(x_first,y_first)
print("x_first_1:",clf.predict([[1]]))
print("x_first_2:",clf.predict([[2]]))
print("x_first_3:",clf.predict([[3]]))
print("x_first_2:",clf.predict([[3]]))
