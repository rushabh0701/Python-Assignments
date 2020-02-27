__author__ = "rushabh"

import matplotlib.pyplot as plt

sc = []
lc = []

def geo():
    x = 0
    while x <= 1:
        lc.append(40 * x + 30 * (1 - x))
        sc.append(48 * x + 40 * (1 - x))
        x += 0.01
    plt.plot(sc)
    plt.plot(lc)
    plt.show()

geo()
