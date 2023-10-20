import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load your dataset (replace 'YourData.csv' with the actual file path)
data = pd.read_csv("/content/diabetes.csv")

# Assuming you have a binary classification problem with features 'X' and binary labels 'y'
X = data.iloc[:,0]
y = data.loc[:,'Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



# Logistic regression parameters
w0 = 0
w1 = 0
m = len(X_train)
learning_rate = 0.01

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

cost_list=[]
iterations=1000
# Logistic regression training
for i in range(iterations):
    z = w0 + np.dot(X_train, w1)
    A = sigmoid(z)

    # Calculate the cost using logistic regression loss function
    cost = -(1/m) * np.sum(y_train * np.log(A) + (1 - y_train) * np.log(1 - A))
    cost_list.append(cost)
    # Compute gradients
    dw0 = (1/m) * np.sum(A - y_train)
    dw1 = (1/m) * np.dot(X_train.T, (A - y_train))

    # Update weights
    w0 -= learning_rate * dw0
    w1 -= learning_rate * dw1

# Print the final cost
print(f"Final Cost: {cost:.4f}")

# Scatter plot of the data points
plt.plot(range(iterations), cost_list)
plt.show()