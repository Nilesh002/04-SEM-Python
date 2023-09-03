import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/content/mytext.txt")
x=data.iloc[:,0]
y=data.iloc[:,1]

c=0
m=0
m=len(x)
a=0.0001
iter=1000

for i in range(iter):
  y_pred=(m*x)+c
  df_m=(2/m)*sum((y_pred-y)*x)
  df_c=(2/m)*sum(y_pred-y)
  c=c-(a*df_c)
  m=m-(a*df_m)

print(c,m)

cost=0

def mse(m,c):
  sum=np.sum((m*x+c-y)**2/(2*m))
  print(f"Sum is {sum}")


cost=np.sum((m*x+c-y)**2/(2*m))

print(f"The cost of the function is {cost}")

plt.scatter(x,y,c='red')
plt.plot(x,y_pred,c='blue')
plt.show
mse(m,c)