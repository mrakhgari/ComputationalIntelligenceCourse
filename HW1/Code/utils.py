#
import numpy as np

# a simple code for nural network


# initialize a model
def init_one_layer_model(input_size, hidden_size):
    model = {}
    # normal distribution for w
    model['W1'] = 0.01 * np.random.randn(hidden_size, input_size)
    model['b1'] = np.zeros((hidden_size,1))  # bios
    return model    

# print(init_one_layer_model(2, 1)['W1'].T)
# print(read_data())
