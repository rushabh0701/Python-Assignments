__author__ = "rushabh"

import math
def drugs(H, L, k):
    T = (1/k)*math.log(H/L)
    return T

print(drugs(2, 0.5, 0.02))