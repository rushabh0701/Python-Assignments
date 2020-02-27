__author__ = "rushabh"
import math
import random

def main():
    n = 1000
    a = 0.5
    b = 1.5
    M = 10
    count = 0
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, M)
        if y <= math.sqrt(x):
            count = count + 1
    print(M*(b-a)*count/n)

main()
