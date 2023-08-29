import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

input_data=pd.read_csv("/content/insurance.csv")

input_data['sex']=input_data['sex'].astype("category")
input_data['sex']=input_data['sex'].cat.codes

input_data['smoker']=input_data['smoker'].astype("category")
input_data['smoker']=input_data['smoker'].cat.codes

input_data['region']=input_data['region'].astype("category")
input_data['region']=input_data['region'].cat.codes

x=input_data.drop('charges',axis=1)
y=input_data.loc[:,'charges']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

# FITTING THE MODEL
model=LinearRegression()
model.fit(x_train,y_train)

# TESTING MODEL FOR TRAINING DATA
x_train_prediction=model.predict(x_train)
x_train_as=r2_score(x_train_prediction,y_train)
print(f"The accuracy rate for training data is {x_train_as*100}")

# TESTING MODEL FOR TESTING DATA
x_test_prediction=model.predict(x_test)
x_test_as=r2_score(x_test_prediction,y_test)
print(f"The accuracy rate for training data is {x_test_as*100}\n")

c=model.intercept_
m=model.coef_

plt.scatter(x_train_prediction,y_train)
plt.xlabel("Predicted label")
plt.ylabel("Original label")

plt.scatter(x_test_prediction,y_test,marker='*',color='black')
plt.show

inp=(33,1,22.705,0,0,1)
inp1=np.array(inp).reshape((1,-1))

# TESTING FOR INPUT DATA
prediction=model.predict(inp1)
print(prediction)