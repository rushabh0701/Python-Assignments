import matplotlib.pyplot as plt

# Rabbit data
rb = 0.75  # birth rate of rabbit
rd = 0.67  # death rate of rabbit
rg = rb - rd  # growth rate
rab = 1000  # Initial rabbit population

# Fox data
fb = 0.5
fd = 0.48

fox = 100  # Initial fox population
a = 0.001
b = 0.002
r = 4.4*10**(-8)
s = 4.4*10**(-8)

list_r = []
list_f = []

print("Initial Population of Rabbit", rab)
print("Initial Population of fox", fox)

for i in range(30):
    dr = rb*rab + a*rab*fox - r*rab*rab
    df = -fb*fox + b*rab*fox - s*fox*fox
    print("New population of rabbit at cycle %d: "%(i+1),int(dr))
    print("New population of fox at cycle %d: "%(i+1),int(df))
    rab = dr
    fox = df
    list_r.append(rab)
    list_f.append(fox)
    
plt.plot(list_r, 'r-', label='Rabbits')
plt.plot(list_f, 'b-', label='Foxes')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Cycles')
plt.ylabel('Population')
plt.title('Evolution of population of X and y')
plt.show()


