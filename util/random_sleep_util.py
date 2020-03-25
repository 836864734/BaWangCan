import time

import numpy as np


def sleep(min_time: int, max_time: int):
    time.sleep(np.random.randint(min_time, max_time))
    pass
