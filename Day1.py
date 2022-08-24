sweep=[]
with open("Problem1.txt") as f:
    while True:
        line=f.readline()
        if not line:
            break
        try:
            sweep.append(int(line))
        except:
            pass
#Part1
"""count=0
for i in range(len(sweep)):
    try:
        if sweep[i]<sweep[i+1]:
            count+=1
    except:
        pass
print(count)"""
#Part2
count=0
for i in range(len(sweep)):
    try:
        if sweep[i]<sweep[i+3]:
            count+=1
    except:
        pass
print(count)