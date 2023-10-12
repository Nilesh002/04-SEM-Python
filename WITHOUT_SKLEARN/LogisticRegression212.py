import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Feature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Label': [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
       }


df = pd.DataFrame(data)

# Separate the feature and label
X_train = df[['Feature']].values
Y_train = df[['Label']].values

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def model(X, Y, a, iterations):
    m, n = X.shape
    w1 = np.zeros((n, 1))
    w0 = 0
    cost_list = []

    for i in range(iterations):
        Z = np.dot(X, w1) + w0
        A = sigmoid(Z)

        cost = -(1/m) * np.sum(Y*np.log(A) + (1-Y)*np.log(1-A))

        dW = (1/m) * np.dot(X.T, (A - Y))
        dB = (1/m) * np.sum(A - Y)
        w1 = w1-a * dW
        w0 = w0-a * dB

        cost_list.append(cost)

        if i % (iterations // 10) == 0:
            print("Cost after", i, "iterations:", cost)

    return w1, w0, cost_list

# Hyperparameters
iterations = 1000
a = 0.01

# Train the model
w1, w0, cost_list = model(X_train, Y_train, a, iterations)

# Plot the cost over iterations
plt.plot(range(iterations), cost_list)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()
