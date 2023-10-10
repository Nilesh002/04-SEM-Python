import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/content/Salary_dataset.csv")
x=data.iloc[:,0]
y=data.iloc[:,1]

w0=0
w1=0
m=len(x)
a=0.0001

for i in range(1000):
  y_pred=(w1*x)+w0
  df_w1=(2/m)*np.sum((y_pred-y)*x)
  df_w0=(2/m)*np.sum(y_pred-y)
  w0=w0-(a*df_w0)
  w1=w1-(a*df_w1)

print(f"The weights are w0={w0} and w1={w1}")

cost=0

def mse(w1,w0):
  sum=np.sum((w1*x+w0-y)**2/(2*m))
  print(f"The cost is {sum}")

plt.scatter(x,y,c='red')
plt.plot(x,y_pred,c='blue')
plt.show
mse(w1,w0)