import numpy as np
with open("Day6.txt") as f:
    line = f.readline()
time_to_birth = [int(i) for i in line.split(",")]
times={}
for i in range(9):
    times[i]=0
for t in time_to_birth:
    times[t]+=1

"""
for day in range(256):
    x=times[0]
    for i in range(6):
        times[i]=times[i+1]
    times[6]=times[7]+x
    times[7]=times[8]
    times[8]=x
total=0
for value in times.values():
    total+=value
"""

#Matrix multiplication
matrix_string="000000101100000000010000000001000000000100000000010000000001000000000100000000010"
a=np.zeros((9,9),dtype=int)
count=0
for i in range(9):
    for j in range(9):
        a[j][i] = int(matrix_string[count])
        count+=1


times_vec = np.zeros((9,1),dtype=int)
for key,value in times.items():
    times_vec[key]=value
result_vec=times_vec
for i in range(1024):
    #result_vec=np.matmul(a,result_vec)
    result_vec=a.dot(result_vec)
a

print(np.sum(result_vec))