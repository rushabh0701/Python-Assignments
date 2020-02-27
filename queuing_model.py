import simpy as sp
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation


#Calculate customer arrival time

#Average arrival rate of customer
lambd = 2 # number of customer per 60 second
mu = 120 # average service time
MIN_PATIENCE = 180 # minimum customer patience
MAX_PATIENCE = 300 # maximum customer patience
i = 0

def poisson_dist(lambd):
    s = np.random.poisson(lambd)
    #print ("Arrival time: ",s)
    return s
    
def expon_dist(mu):
    e = np.random.exponential(mu)
    #print ("Service time: ",e)
    return e
    

def new_customer(env,interval,count):
    while True:
        c = []
        pos_dist = poisson_dist(lambd)
        print("Customer arrived: ", pos_dist)
        for i in range(pos_dist):
            c.append(cust(env, 'Customer %d' % i, count))
            env.process(c[i])
            t = env.now + float(interval)
            yield env.timeout(t)
    
def cust(env,name,count):
    """Customer comes in, gets item, gets into queue and is served"""
    cust_arrive = env.now
    print("%d: %s arrives" % (cust_arrive,name))
    
    with count.request() as req:
        patience = random.uniform(MIN_PATIENCE,MAX_PATIENCE)
        results = yield req | env.timeout(patience)
        
        wait = env.now - cust_arrive
        
        if req in results:
            print("%7.4f %s: waited %6.3f" %(env.now,name,wait))
            
            tib = expon_dist(mu)
            yield env.timeout(tib)
            print("%7.4f %s: Finished" %(env.now,name))
        else:
            print("%7.4f %s: left the queue" % (env.now, name))
            

p=poisson_dist(lambd)
m = expon_dist(mu)

######################################
##Animation for graph

n, bins = np.histogram(p, 100)
n2, bins2 = np.histogram(m, 100)
# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)
nverts = nrects * (1 + 3 + 1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom


left2 = np.array(bins2[:-1])
right2 = np.array(bins2[1:])
bottom2 = np.zeros(len(left2))
top2 = bottom2 + n2
nrects2 = len(left2)
nverts2 = nrects2 * (1 + 3 + 1)
verts2 = np.zeros((nverts2, 2))
codes2 = np.ones(nverts2, int) * path.Path.LINETO
codes2[0::5] = path.Path.MOVETO
codes2[4::5] = path.Path.CLOSEPOLY
verts2[0::5, 0] = left2
verts2[0::5, 1] = bottom2
verts2[1::5, 0] = left2
verts2[1::5, 1] = top2
verts2[2::5, 0] = right2
verts2[2::5, 1] = top2
verts2[3::5, 0] = right2
verts2[3::5, 1] = bottom2

patch = None
patch2 = None

def animate(i):
    # simulate new data coming in
    currpos = poisson_dist(lambd)
    n, bins = np.histogram(currpos, 100)
    top = bottom + n
    verts[1::5, 1] = top
    verts[2::5, 1] = top
    return [patch, ]


def animate2(i):
    # simulate new data coming in
    currsvc = np.random.exponential(240, 1000)
    currsvc = expon_dist(mu)
    n2, bins2 = np.histogram(currsvc, 100)
    top2 = bottom2 + n2
    verts2[1::5, 1] = top2
    verts2[2::5, 1] = top2
    return [patch2, ]
######################################################

env = sp.Environment()

count = sp.Resource(env,capacity=2)
env.process(new_customer(env,m,count))
env.run()


#######################################################
##Plot data
fig, ax = plt.subplots()
barpath = path.Path(verts, codes)
patch = patches.PathPatch(
    barpath, facecolor='green', edgecolor='yellow', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

ani = animation.FuncAnimation(fig, animate, 100, repeat=False, blit=True)

fig2, ax2 = plt.subplots()
barpath2 = path.Path(verts2, codes2)
patch2 = patches.PathPatch(
    barpath2, facecolor='green', edgecolor='yellow', alpha=0.5)
ax2.add_patch(patch2)

ax2.set_xlim(left2[0], right2[-1])
ax2.set_ylim(bottom2.min(), top2.max())

ani2 = animation.FuncAnimation(fig2, animate2, 100, repeat=False, blit=True)
plt.show()
###############################################################
