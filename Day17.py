from collections import defaultdict
from time import perf_counter, perf_counter, process_time, time
import pandas as pd
from math import ceil, floor
import numpy as np
import matplotlib.pyplot as plt
x_min=201;x_max=230;y_min=-99;y_max=-65
#Part1
"""
poly=[1,1, -x_max*2]
x_velo_max=max(np.roots(poly))
poly=[1,1, -x_min*2]
x_velo_min=max(np.roots(poly))
possible_x=[i for i in range(ceil(x_velo_min),floor(x_velo_max)+1)]
y_velo_cmax=abs(y_min)-1
y_velo_min=abs(y_max)-1




max_height=y_velo_cmax*(y_velo_cmax+1)//2
"""
"""
x_axis=[i*(i+1)/2 for i in range(x_velo+1)][::-1]
x_axis=[int(max(x_axis)-x) for x in x_axis]
y_up=[int(i*(i+1)/2) for i in range(y_velo+1)][::-1]
y_up=[[int(max(y_up)-y) for y in y_up]]
y_down=y_up[::-1]
y_speed=[i for i in range(-11,-20,-1)]
y_hell=[sum(y_speed[0:n]) for n in range(10)]
"""
"""
poly=[1,1, -x_min*2]
x_velo_min=max(np.roots(poly))

y_velo_max=abs(y_min)-1
y_velo_min=y_min
x_velo_min=floor(x_velo_min)
x_velo_max=x_max
y_range=[y for y in range(y_velo_min,y_velo_max+1)]
x_range=[x for x in range(x_velo_min,x_velo_max+1)]
velo_range=[ (x,y) for x in x_range for y in y_range]
def tracker(x_velo,y_velo):
    t=0
    r=(-(t**2)/2+x_velo*t if t<=x_velo else  (x_velo**2)/2,-(t**2)/2+y_velo*t)
    while r[0]<x_max and r[1]>y_min:
        r=(-(t**2)/2+x_velo*t if t<=x_velo else  (x_velo**2)/2,-(t**2)/2+y_velo*t)
        if x_min<=r[0]<=x_max and y_min<=r[1]<=y_max:
            return True
        t+=1
    return False
    """
"""
hit_count=0
for x,y in velo_range:
    if tracker(x,y):
        hit_count+=1

"""

#Even more optimization

t1=process_time()
y_step_dictionary=defaultdict(set)

y_step=1
negative_velocities=[1]
while len(negative_velocities)>0 :
    #Instead of throwing with down with v we can throw up with v-1. So positives can be counted from negatives.2*(-v-1)+1+y_step total steps for positive one.
    #y_min<=y_step*y_velo-(y_step*(y_step-1))/2<=y_max what y_velos that satisfy this while len(velocities)>0:
    #y_min+(y_step*(y_step-1))/2<=y_step*y_velo<=y_max+(y_step*(y_step-1))/2
    #So integer number of velocities that hit area are integers in [(y_min+(y_step*(y_step-1))/2)/y_step,(y_max+(y_step*(y_step-1))/2)/y_step]
    #We want negative ones so:
    negative_velocities=[y_velo for y_velo in range(ceil((y_min+(y_step*(y_step-1))/2)/y_step),min(0,floor((y_max+(y_step*(y_step-1))/2)/y_step)+1))]
    for velo in negative_velocities:
        y_step_dictionary[y_step].add(velo)
        y_step_dictionary[-2*velo-1+y_step].add(-velo-1)
    y_step+=1
y_step_dictionary=dict(sorted(y_step_dictionary.items()))


x_step_dictionary={}
#x_min<=x_step*x_velo-(x_step*(x_step-1))/2 if x_step<x_velo else (x_velo**2)/2+x_velo/2 <=x_max what x_velos that satisfy this
#x_min+(x_step*(x_step-1))/2<=x_step*x_velo<=x_max+(x_step*(x_step-1))/2 for velocities that did not stop before that is x_step<x_velo
#That is same as y but when we se

stops=[]
for x_step in y_step_dictionary.keys():
    velocities=[]
    velocities+=stops
    interval=list(range(max(ceil((x_min+(x_step*(x_step-1))/2)/x_step),x_step),floor((x_max+(x_step*(x_step-1))/2)/x_step)+1))
    if len(interval)>0:
        for x_velo in interval:
            velocities.append(x_velo)
            if x_velo==x_step:
                stops.append(x_velo)
    x_step_dictionary[x_step]=velocities
    

velocity_pairs=[]
for step in x_step_dictionary.keys():
    velocity_pairs+=[(x,y) for x in x_step_dictionary[step] for y in y_step_dictionary[step]]
#Convert to set so we dont count twice 
velocity_pairs=set(velocity_pairs)
t2=process_time()
#print(len(set(velocity_pairs)))


"""
#FOR TESTING
my_sol=set(velocity_pairs)
df = pd.read_table("Solution.txt",header=None,dtype=str,delim_whitespace=True)
solution=set()
for x in range(9):
    for y in range(13):
        if type(df[x][y])==str:
            solution.add((int(df[x][y].split(",")[0]),int(df[x][y].split(",")[1])))
print(x_step_dictionary)
print(y_step_dictionary)
print(solution.difference(my_sol))
print(solution==my_sol)
"""
#Last
t3=process_time()
excess_step_dictionary=defaultdict(set)
velocity_pairs=set()
step=1
negative_velocities=[1]
stops=[]
while len(negative_velocities)>0 :
    #Instead of throwing with down with v we can throw up with v-1. So positives can be counted from negatives.2*(-v-1)+1+y_step total steps for positive one.
    #y_min<=y_step*y_velo-(y_step*(y_step-1))/2<=y_max what y_velos that satisfy this while len(velocities)>0:
    #y_min+(y_step*(y_step-1))/2<=y_step*y_velo<=y_max+(y_step*(y_step-1))/2
    #So integer number of velocities that hit area are integers in [(y_min+(y_step*(y_step-1))/2)/y_step,(y_max+(y_step*(y_step-1))/2)/y_step]
    #We want negative ones so:
    negative_velocities=list(range(ceil((y_min+(step*(step-1))/2)/step),min(0,floor((y_max+(step*(step-1))/2)/step)+1)))
    interval=list(range(max(ceil((x_min+(step*(step-1))/2)/step),step),floor((x_max+(step*(step-1))/2)/step)+1))
    if len(interval)>0:
        for x_velo in interval:
            if x_velo==step:
                stops.append(x_velo)
    for velo in negative_velocities:
        excess_step_dictionary[-2*velo-1+step].add(-velo-1)
        for x_velo in interval:
            velocity_pairs.add((x_velo,velo))
    
    step+=1
for step in reversed(excess_step_dictionary.keys()):
    interval=list(range(max(ceil((x_min+(step*(step-1))/2)/step),step),floor((x_max+(step*(step-1))/2)/step)+1))
    if len(interval)>0:
        for x_velo in interval:
            if x_velo==step:
                stops.append(x_velo)
            else:
                for y_velo in excess_step_dictionary[step]:
                    velocity_pairs.add((x_velo,y_velo))
    for y_velo in excess_step_dictionary[step]:
        for x_velo in stops:
            velocity_pairs.add((x_velo,y_velo))
t4=process_time()
print(t2-t1,t4-t3)



   