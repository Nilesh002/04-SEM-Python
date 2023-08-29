import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model_score=pd.read_csv('/content/iris.csv')

x=model_score.drop('Species',axis=1)
y=model_score.loc[:,'Species']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)

model=LogisticRegression()
model.fit(x_train,y_train)


'''TEST THE MODEL BASED ON TRAINING DATA  '''

x_train_pred=model.predict(x_train)
x_train_as=accuracy_score(x_train_pred,y_train)

print(x_train_as*100)

x_test_pred=model.predict(x_test)
x_test_as=accuracy_score(x_test_pred,y_test)
print(x_test_as*100)

input_data=(6.7,3,5.2,2.3)
inp=np.array(input_data).reshape((1,-1))
print(inp)

xu=model.predict(inp)
print(xu)