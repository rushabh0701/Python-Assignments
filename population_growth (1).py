import math 
import numpy as np
import matplotlib.pyplot as plt

## Rabbit data
rb = 0.75 ## birth rate of rabbit
rd = 0.67 ## death rate of rabbit
rg = rb - rd ## growth rate
rab = 1000 ## Initial rabbit count

## Mice Data
mb = 0.7 ## birth rate of mice
md = 0.55 ## death rate of mice
mice = 500 ## Initial mice count

## Fox data
fb = 0.5
fd = 0.48

fox = 100 ## Initial fox count
a = 0.001
b = 0.002
c = 0.0002
d = 0.002

r = 4.4*10**(-8)
s = 4.4*10**(-8)
t = 4.4*10**(-8)

list_r = []
list_f = []
list_m = []

print("Initial Population of Rabbit", rab)
print("Initial Population of fox", fox)
print("Initial Population of mice", mice)

for i in range(15):
    dr = rb*rab - a*rab*fox - r*rab*rab
    dm = mb*mice - c*mice*fox - t*mice*mice
    df = -fb*fox + b*rab*fox + d*mice*fox - s*fox*fox
    print("New population of rabbit at cycle %d: "%(i),int(dr))
    print("New population of mice at cycle %d: "%(i),int(dm))
    print("New population of fox at cycle %d: "%(i),int(df))
    rab = dr
    mice = dm
    fox = df
    list_r.append(rab)
    list_m.append(mice)
    list_f.append(fox)
    
plt.plot(list_r, 'r-', label='Rabbits')
plt.plot(list_m, 'g-', label='Mice')
plt.plot(list_f, 'b-', label='Foxes')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Cycles')
plt.ylabel('Population')
plt.title('Evolution of population of X and y')
plt.show()
#rab_new_pop = int(rab*math.exp(rg*t))
#fox_new_pop = int(fox*math.exp(fg*t))

