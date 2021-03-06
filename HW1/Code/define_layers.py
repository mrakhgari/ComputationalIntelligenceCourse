# define training constants
import numpy as np
from LinearLayer import LinearLayer
from compute_bce_cost import compute_bce_cost
from read_data import read_data
import random
from plot import create_plot

learning_rate = 4
number_of_epochs = 100



# np.random.seed(20)  # set seed value so that the results are reproduceable
# (weights will now be initailzaed to the same pseudo-random numbers, each time)

# Our network architecture has the shape:
#                       (input)--> [Linear->Sigmoid] -->(output)

X_train, X_test, Y_train, Y_test = read_data()

# ------ LAYER-1 ----- define output layer that takes in training data
Z1 = LinearLayer(input_shape=X_train.shape, n_out=2)
Z2 = LinearLayer(input_shape=Z1.Z.shape, n_out=1)

costs = []  # initially empty list, this will store all the costs after a certain number of epochs
# for i in range(20):
#     lr = 10 ** random.uniform(0,1)
# Start training
for epoch in range(number_of_epochs):

    # ------------------------- forward-prop -------------------------
    Z1.forward(X_train)
    Z2.forward(Z1.Z)
    # ---------------------- Compute Cost ----------------------------
    cost, dA2, accuracy_rate, nn = compute_bce_cost(Y_train, Z2.Z)
    # print and store Costs every 100 iterations and of the last iteration.
    # if (epoch % 100) == 0 or epoch == number_of_epochs - 1:
    print("Cost at epoch#{}: {} and accuracy {}".format(
        epoch, cost, accuracy_rate))
    costs.append(cost)
    print(nn)

    # ------------------------- back-prop ----------------------------
    Z2.backward(dA2)
    Z1.backward(Z2.dPervious)

    # ----------------------- Update weights and bias ----------------
    Z2.update_params(learning_rate=learning_rate)
    Z1.update_params(learning_rate=learning_rate)

# Start testing
Z1.forward(X_test)
Z2.forward(Z1.Z)
# ---------------------- Compute Cost ----------------------------
cost, dA1, accuracy_rate, d = compute_bce_cost(Y_test, Z2.Z)
print("index is: {} with cost {} and accuracy_rate {} -> lr {}".format(
    1, cost, accuracy_rate, learning_rate))

create_plot(X_test, np.array(d))
