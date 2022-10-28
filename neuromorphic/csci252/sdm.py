import numpy as np


class SDM:
    """
    :param p: Number of patterns.
    :param n: Size of memory address and data vectors.
    """
    def __init__(self, p, n):
        self.p = p
        self.n = n
        # radius of neighborhood search
        self.radius = 0.451 * n

        self.addresses = np.random.randint(0, 2, size=(p, n))
        self.data = np.zeros((p, n))

    def enter(self, address):
        # loop over all addresses
        for i in range(self.p):
            memory_addy = self.addresses[i]
            
            # if address within key...
            if self._dist(memory_addy, address) < self.radius:
                # ...add key to mapped data
                self.data[i] += 2 * address - 1

    def lookup(self, address):
        data_val = np.zeros(self.n)
        # loop over all addresses
        for i in range(self.p):
            memory_addy = self.addresses[i]

            # if address within key...
            if self._dist(memory_addy, address) < self.radius:
                # ...add mapped data to return value
                data_val += self.data[i]
        
        return (data_val > 0).astype(int)

    def _dist(self, p, q):
        # hamming distance
        return (p != q).astype(int).sum()


def plot(img_flat, cols=16):
    rows = img_flat.shape[0] // cols
    for i in range(rows):
        for j in range(cols):
            val = img_flat[i * cols + j]
            if val == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def noisy_copy(patterns, prob=0.5):
    flip = (np.random.rand(*patterns.shape) < prob).astype(int)
    return np.bitwise_xor(patterns, flip)


def ring():
    r = [0] * 5 + [1] * 6 + [0] * 5
    r += [0] * 3 + [1] * 10 + [0] * 3
    r += [0] * 2 + [1] * 4 + [0] * 4 + [1] * 4 + [0] * 2
    r += [0] * 1 + [1] * 4 + [0] * 6 + [1] * 4 + [0] * 1
    r += [0] * 1 + [1] * 3 + [0] * 8 + [1] * 3 + [0] * 1
    r += [1] * 3 + [0] * 10 + [1] * 3
    r += [1] * 3 + [0] * 10 + [1] * 3
    r += [1] * 3 + [0] * 10 + [1] * 3
    r += list(reversed(r))
    return np.array(r)


if __name__ == "__main__":
    # r = ring()
    # plot(r, 16)

    # sdm = SDM(p=2000, n=256)
    # sdm.enter(r)

    # new_r = sdm.lookup(r)
    # plot(new_r, 16)

    # noisy_r = noisy_copy(r, prob=0.25)
    # plot(noisy_r, 16)
    # plot(sdm.lookup(noisy_r), 16)

    sdm = SDM(p=2000, n=256)
    r = ring()

    for i in range(5):
        noisy_r = noisy_copy(r, prob=0.1)
        sdm.enter(noisy_r)
        plot(noisy_r, 16)
        print()

    noisy_r = noisy_copy(r, prob=0.1)
    ideal_r = sdm.lookup(noisy_r)

    plot(ideal_r, 16)
