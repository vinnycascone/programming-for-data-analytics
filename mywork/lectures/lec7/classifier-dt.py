import pandas as pd

dataurl = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

irisdf= pd.read_csv(dataurl)
print(irisdf.head(3))

colnames=["sepal.length","sepal.width","petal.length","petal.width"]
x=irisdf[colnames]
y= irisdf["variety"]

from sklearn import tree

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

print(clf.predict([[1,3,4,5]]))