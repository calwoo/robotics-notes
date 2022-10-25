import time
import random

import numpy as np


def random_elements():
    return [random.random() for _ in range(1000000)]

rlist1 = random_elements()
rlist2 = random_elements()

def dot_prod(l1, l2):
    assert len(l1) == len(l2)
    sum_ = 0
    for a, b in zip(l1, l2):
        sum_ += a * b
    return sum_

start = time.time()
print(dot_prod(rlist1, rlist2))

print(f"that took {time.time() - start} secs")

rlist1_np = np.asarray(rlist1)
rlist2_np = np.asarray(rlist2)

start = time.time()
print(np.dot(rlist1_np, rlist2_np))

print(f"that took {time.time() - start} secs")
