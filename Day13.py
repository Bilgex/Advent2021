import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df = pd.read_table("Day13.txt",header=None,dtype=str)
size_x=0
size_y=0
point_list=[]
fold_list=[]
for data in df[0]:
    try:
        x,y=data.split(",")
        point_list.append((int(x),int(y)))
        size_x=max(int(x),size_x)
        size_y=max(int(y),size_y)
    except ValueError:
        axis,pos=data.replace("fold along ","").split("=")
        fold_list.append((axis,int(pos)))
paper=np.zeros((size_y+1,size_x+1),dtype=int)
for point in point_list:
    y,x=point
    paper[x,y]=1
#Part1
"""
fold_axis,fold_num = fold_list[0]
flipped_paper =np.flip(paper,0 if fold_axis=="x" else 1)
final_paper=paper+flipped_paper
if fold_axis=="x":
    final_paper=final_paper[:fold_num,:]
else:
    final_paper=final_paper[:,:fold_num]
print(np.count_nonzero(final_paper))
"""
for instruction in fold_list:
    fold_axis,fold_num = instruction
    flipped_paper =np.flip(paper,1 if fold_axis=="x" else 0)
    final_paper=paper+flipped_paper
    if fold_axis=="y":
        final_paper=final_paper[:fold_num,:]
    else:
        final_paper=final_paper[:,:fold_num]
    paper=final_paper

paper=paper>0
fig,ax =plt.subplots()
im =ax.imshow(paper)
plt.savefig("paper.png")