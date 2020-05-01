import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def create_plot(X_data, Y_data):
    """
    This function prints a scooter diagram for X1 and X2 data
    Args:
        X_data: points
        Y_data: labels of data
    """
    cmap = matplotlib.colors.ListedColormap(["red", "blue"], N=None)
    # scattter plot
    scatter = plt.scatter(X_data.T[:, 0], X_data.T[:, 1],
                          s=100, c=np.squeeze(Y_data.T),
                          marker='.', cmap=cmap)  # s-> size of marker

    plt.xlabel('x1', size=10)
    plt.ylabel('x2', size=10)
    plt.axhline(0, color='black')  # x-axis line
    plt.axvline(0, color='black')  # y-axis line

    plt.legend(scatter.legend_elements()[0], ['0', '1'])

    plt.show()
