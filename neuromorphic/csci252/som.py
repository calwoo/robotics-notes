import numpy as np
import matplotlib.pyplot as plt


class SOM:
    """
    :param m: Size of grid.
    :param n: Dimension of weights.
    """

    def __init__(self, m=10, n=2):
        self.m = m
        self.n = n

        # not sure why the clustering, but okay
        self.weights = np.random.random((m, m, n)) / 10 + 0.45

    def learn(self, data, T, a0, d0):
        """
        :param data: Training data.
        :param T: Number of training interations.
        :param a0: Initial learning rate.
        :param d0: Initial neighborhood distance.
        """

        num_data = len(data)
        for t in range(T):
            # calculate current neighborhood radius
            d = d0 * (1 - t / float(T))

            # calculate current learning rate
            a = a0 * (1 - t / float(T))

            # randomly pick input from training set
            data_idx = np.random.randint(low=0, high=num_data)
            data_pt = data[data_idx]

            # find best matching unit
            best_i, best_j = self._find_bmu(data_pt)

            # loop over the neighbors of the BMU, adjusting their weights
            neighbors = self._get_neighbors((best_i, best_j), d)
            for x, y in neighbors:
                self.weights[x, y] += a * (data_pt - self.weights[x, y])

    def _find_bmu(self, inp):
        best_dist = float("inf")
        best_i, best_j = 0, 0
        for i in range(self.m):
            for j in range(self.m):
                weight = self.weights[i, j]
                dist = np.sqrt(np.sum((inp - weight) ** 2))
                if dist < best_dist:
                    best_dist = dist
                    best_i = i
                    best_j = j
        return best_i, best_j

    def _get_neighbors(self, center, radius):
        neighbors = []
        center_x, center_y = center
        for i in range(self.m):
            for j in range(self.m):
                dist = np.sqrt((i - center_x)**2 + (j - center_y)**2)
                if dist < radius:
                    neighbors.append((i, j))
        return neighbors


if __name__ == "__main__":
    data = np.random.random((5000, 2))
    som = SOM(m=10, n=2)
    som.learn(data, T=5000, a0=1, d0=2)

    plt.scatter(data[:, 0], data[:, 1], s=0.2)
    
    # plot SOM weights
    for i in range(som.m):
        for j in range(som.m):
            plt.plot(som.weights[i, j, 0], som.weights[i, j, 1], "ro")

    plt.gca().set_aspect("equal")
    plt.show()


