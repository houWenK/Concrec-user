import numpy as np

def bucketize(user_id, n):
    if user_id is None:
        return 0

    rng = np.random.default_rng(user_id * 9)
    return int(rng.integers(low=0, high=n))
