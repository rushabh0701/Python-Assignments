__author__ = "rushabh"
import random

def Inventory(Q, T, d, s, N):
    K = N
    I = 0
    C = 0
    q = 0
    flag = 0
    unfulfilled = 0
    days_without_gas = 0

    while flag == 0:
        I = I + Q
        C = C + d

        if T >=  K:
            T = K
            flag += 1

        for i in range(1, T+1):
            x = random.uniform(0,1)

            if 0 <= x < 0.01:
                q = (x + 0.02)*5000
            elif 0.01 <= x < 0.03:
                q = (x + 0.2)*5000
            elif 0.03 <= x < 0.08:
                q = (x + 0.545)*2000
            elif 0.08 <= x < 0.2:
                q = (x + 1.42)*833.33
            elif 0.2 <= x < 0.4:
                q = (x + 2.5)*500
            elif 0.4 <= x < 0.67:
                q = (x + 3.515)*370.37
            elif 0.67 <= x < 0.85:
                q = (x + 2.12)*555.55
            elif 0.85 <= x < 0.93:
                q = (x + 0.47)*1250
            elif 0.93 <= x < 0.97:
                q = (x - 0.23)*2500
            elif 0.97 <= x <= 1:
                q = (x - 0.6)*5000


            if q > I:
                unfulfilled += q - I

            I = I - q

            if I <= 0:
                I = 0
                days_without_gas += 1
            else:
                C = C +  I * s

            K -= 1
    c = C/N
    print("Average daily cost: {}".format(c))

Inventory(7500, 10, 5000, 3, 100)