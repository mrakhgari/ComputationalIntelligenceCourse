import numpy as np  # import numpy library
from utils import init_one_layer_model


class LinearLayer:
    """
      This Class implements all functions to be executed by a linear layer
      in a computational graph
      Args:
          input_shape: input shape of Data/Activations
          n_out: number of neurons in layer

      Methods:
          forward(A_prev)
          backward(upstream_grad)
          update_params(learning_rate)
    """

    def __init__(self, input_shape, n_out):
        # number of examples in training data
        self.example_size = input_shape[1]
        # `params` store weights and bias in a python dictionary
        self.params = init_one_layer_model(input_shape[0], n_out)
        # create space for resultant Z output
        self.Z = np.zeros((self.params['W1'].shape[0], input_shape[1]))
        self.dW = 0
        self.db = 0
        self.dPervious = 0

    def forward(self, pervious):
        """
        This function performs the forwards propagation using activations from previous layer
        Args:
            pervious:  Activations/Input Data coming into the layer from previous layer
        """

        self.pervious = pervious
        self.Z = np.dot(self.params['W1'], self.pervious) + self.params['b1']
        self.sigmoid()

    def sigmoid(self):
        """
        This function performs the forwards propagation step through the activation function
        Args:
            Z: input from previous (linear) layer
        """
        self.Z = 1 / (1 + np.exp(-self.Z))

    def backward(self, upstream_grad):
        """"
        This function performs the back propagation using upstream gradients
        Args:
           upstream_grad: gradient coming in from the upper layer to couple with local gradient
        """

        self.dW += np.dot(upstream_grad, self.pervious.T)

        self.db += np.sum(upstream_grad, axis=1, keepdims=True)

        self.dPervious = np.dot(
            self.params['W1'].T, upstream_grad) * self.Z * (1-self.Z)

    def update_params(self, learning_rate):
        """
        This function performs the gradient descent update
        Args:
            learning_rate: learning rate hyper-param for gradient descent
        """

        self.params['W1'] -= (learning_rate * self.dW) / self.example_size
        self.params['b1'] -= (learning_rate * self.db) / self.example_size
