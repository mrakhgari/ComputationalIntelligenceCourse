#
import numpy as np
import pandas as pd
from csv import reader

# a simple code for nural network


# initialize a model
def init_one_layer_model(input_size, hidden_size):
    model = {}
    # normal distribution for w
    model['W1'] = 0.0001 * np.random.randn(input_size, hidden_size)
    model['b1'] = np.zeros(hidden_size)  # bios
    return model


# read csv file as a list of lists
def read_data():
    with open('Resources/dataset.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        csv_list = [y for y in csv_reader]
        df = pd.DataFrame(csv_list[1:])
        return df[df.columns[0:2]], df[df.columns[2]]  # return x and y.


# Calculate the derivative of an neuron output
def transfer_derivative(sigmoid):
    return sigmoid * (1.0 - sigmoid)


# sigmoid function
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))


print(init_one_layer_model(2, 1)['W1'].T)
# print(read_data())
print(sigmoid_function(0))
