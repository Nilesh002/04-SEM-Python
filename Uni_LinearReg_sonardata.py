import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

sonar_data=pd.read_csv("Copy of sonar data.csv" , header=None)

x=sonar_data.drop(60,axis=1)
y=sonar_data[60]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)

model=LogisticRegression()
model.fit(x_train,y_train)

x_train_pred=model.predict(x_train)
train_data_as=accuracy_score(x_train_pred,y_train)
print(f"\nThe Accuracy Score of Training Data is {train_data_as*100}")

x_test_pred=model.predict(x_test)
test_data_as=accuracy_score(x_test_pred,y_test)
print(f"The Accuracy Score of Test Data is {test_data_as*100}")

# TESTING THE PREDICTABILITY OF THE MODEL

input=(0.0067,0.0096,0.0024,0.0058,0.0197,0.0618,0.0432,0.0951,0.0836,0.1180,0.0978,0.0909,0.0656,0.0593,0.0832,0.1297,0.2038,0.3811,0.4451,0.5224,0.5911,0.6566,0.6308,0.5998,0.4958,0.5647,0.6906,0.8513,1.0000,0.9166,0.7676,0.6177,0.5468,0.5516,0.5463,0.5515,0.4561,0.3466,0.3384,0.2853,0.2502,0.1641,0.1605,0.1491,0.1326,0.0687,0.0602,0.0561,0.0306,0.0154,0.0029,0.0048,0.0023,0.0020,0.0040,0.0019,0.0034,0.0034,0.0051,0.0031)
input_data=np.array(input).reshape((1,-1))

prediction=model.predict(input_data)
print(f"The Prediction to the input data is {prediction}\n")