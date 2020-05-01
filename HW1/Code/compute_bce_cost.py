import numpy as np


def compute_bce_cost(Y, P_hat):
    """
    This function computes Binary Cross-Entropy(bce) Cost and returns the Cost and its
    derivative.
    This function uses the following Binary Cross-Entropy Cost defined as:
    => - np.sum(Y*np.log(P_hat) + (1-Y)*np.log(1-P_hat))
    Args:
        Y: labels of data
        P_hat: Estimated output probabilities from the last layer, the output layer
    Returns:
        cost: The Binary Cross-Entropy Cost result
        dP_hat: gradient of Cost w.r.t P_hat
    """

    m = len(Y[0])
    for i in range(P_hat.shape[0]):
        for j in range(P_hat.shape[1]):
            if P_hat[i][j] == 1:
                P_hat[i][j] = .999
            if P_hat[i][j] == 0:
                P_hat[i][j] = .001
    d = [0 if i < 0.5 else 1 for i in P_hat[0]]

    cost = -1 * np.sum(Y * np.log(P_hat) + (1-Y) * np.log(1-P_hat))
    # remove extraneous dimensions to give just a scalar (e.g. this turns [[17]] into 17)
    cost = np.squeeze(cost)
    dP_hat = (-1) * ((Y/P_hat) + ((1-Y)/(1-P_hat)))
    print(d)
    print(Y)
    return cost, dP_hat, np.sum(d == Y[0]) / m
