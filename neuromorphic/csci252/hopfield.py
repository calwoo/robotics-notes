import numpy as np
import matplotlib.pyplot as plt


def show_confusion(patterns_1, patterns_2):
    num_patterns = len(patterns_1)
    for i in range(num_patterns):
        for j in range(i + 1):
            cosine = vector_cosine(patterns_1[i], patterns_2[j])
            print(f"{cosine:.2}", end=" ")
        print()

def noisy_copy(patterns, prob=0.5):
    flip = (np.random.rand(*patterns.shape) < prob).astype(int)
    return np.bitwise_xor(patterns, flip)

def vector_cosine(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


class Hopfield:
    """
    :param n: Size of input vector.
    """

    def __init__(self, n):
        self.T = np.zeros((n, n))
    
    def learn(self, patterns):
        for p in patterns:
            centered_p = 2 * p.ravel() - 1
            dT = np.outer(centered_p, centered_p)
            self.T += dT
        
        # zero out diagonal
        np.fill_diagonal(self.T, 0)

    def test(self, pattern, iters=5):
        u = pattern.ravel()
        for t in range(iters):
            u = (np.dot(u, self.T) > 0).astype(int)
        return u

if __name__ == "__main__":
    patterns = np.random.randint(0, 2, size=(5, 30))
    show_confusion(patterns, patterns)

    noisy_patterns = noisy_copy(patterns, prob=0.25)
    show_confusion(noisy_patterns, patterns)

    # train a hopfield net
    net = Hopfield(n=30)
    net.learn(patterns)

    print("no noise recovery")
    reconstructed_pattern = net.test(patterns[0])
    print(patterns[0])
    print(reconstructed_pattern)
    print(f"vector cosine: {vector_cosine(patterns[0], reconstructed_pattern)}")

    print("25% noise recovery")
    reconstructed_noisy_pattern = net.test(noisy_patterns[0])
    print(patterns[0])
    print(noisy_patterns[0])
    print(reconstructed_noisy_pattern)
    print(f"vector cosine: {vector_cosine(patterns[0], reconstructed_noisy_pattern)}")