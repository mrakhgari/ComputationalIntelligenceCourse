# define training constants
import numpy as np
from LinearLayer import *
from SigmoidLayer import *
from compute_bce_cost import *
from csv import reader
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib

# read csv file as a list of lists
df = pd.read_csv('Resources/dataset.csv', names=['x1', 'x2', 'label'])
learning_rate = 0.0001
number_of_epochs = 5000

# np.random.seed(48)  # set seed value so that the results are reproduceable
# (weights will now be initailzaed to the same pseudo-random numbers, each time)

# Our network architecture has the shape:
#                       (input)--> [Linear->Sigmoid] -->(output)

# X_train, Y_train = read_data()
train, test = train_test_split(df, test_size=0.1)
print(test)
X_train, Y_train = train.to_numpy()[:, [0, 1]], train['label'].to_numpy()
X_test, Y_test = test.to_numpy()[:, [0, 1]], test['label'].to_numpy()


# ------ LAYER-1 ----- define output layer that takes in training data
Y_train = Y_train.reshape((162, 1))
Y_test = Y_test.reshape((18, 1))

X_train = X_train.T
Y_train = Y_train.T

X_test = X_test.T
Y_test = Y_test.T

Z1 = LinearLayer(input_shape=X_train.shape, n_out=1)
A1 = SigmoidLayer(Z1.Z.shape)


cmap = matplotlib.colors.ListedColormap(["red", "blue"], N=None)
# scattter plot
scatter = plt.scatter(X_test.T[:, 0], X_test.T[:, 1],
            s=200, c=np.squeeze(Y_test.T),
            marker='.', cmap=cmap)  # s-> size of marker


plt.xlabel('x1', size=10)
plt.ylabel('x2', size=10)
plt.axhline(0, color='black')  # x-axis line
plt.axvline(0, color='black')  # y-axis line

plt.legend(scatter.legend_elements()[0], ['0', '1'])

plt.show()


costs = []  # initially empty list, this will store all the costs after a certain number of epochs

# Start training
for epoch in range(number_of_epochs):

    # ------------------------- forward-prop -------------------------
    Z1.forward(X_train)
    A1.forward(Z1.Z)

    # ---------------------- Compute Cost ----------------------------
    cost, dA1, accuracy_rate = compute_bce_cost(Y_train, A1.A)
    # print and store Costs every 100 iterations and of the last iteration.
    if (epoch % 100) == 0 or epoch == number_of_epochs - 1:
        print("Cost at epoch#{}: {} and accuracy {}".format(
            epoch, cost, accuracy_rate))
        costs.append(cost)

    # ------------------------- back-prop ----------------------------
    A1.backward(dA1)
    Z1.backward(A1.dZ)

    # ----------------------- Update weights and bias ----------------
    Z1.update_params(learning_rate=learning_rate)


Z1.forward(X_test)
A1.forward(Z1.Z)

# ---------------------- Compute Cost ----------------------------
cost, dA1, accuracy_rate = compute_bce_cost(Y_test, A1.A)
print(cost, accuracy_rate)