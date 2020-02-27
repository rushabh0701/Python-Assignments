__author__ = "rushabh"

import matplotlib.pyplot as plt

pop = 6000000
br = 0.0005
dr = 0.0020
mr = 0.0007
pops = []

for i in range(1000):
    pop += (br * pop) - (dr * pop) + (mr * pop)
    pops.append(pop)

plt.plot(pops)
plt.show()