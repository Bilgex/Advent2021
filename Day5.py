import pandas as pd
df=pd.read_table("Day5.txt",header=None,delimiter=" -> ")
def marker(point1,point2):
    x1,y1=int(point1.split(",")[0]),int(point1.split(",")[1])
    x2,y2=int(point2.split(",")[0]),int(point2.split(",")[1])
    marked=[]
    if x1==x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            marked.append((x1,y))
    if y1==y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            marked.append((x,y1))
    if abs(y1-y2)==abs(x1-x2):
        xcrement=int((x2-x1)/abs(x2-x1))
        ycrement=int((y2-y1)/abs(y2-y1))
        for i in range(abs(x2-x1)+1):
            marked.append((x1+xcrement*i,y1+ycrement*i))
    return marked
lines=set()
intersections=set()
for i in range(len(df)):
    line=marker(df[0].iloc[i],df[1].iloc[i])
    for point in line:
        if point not in lines:
            lines.add(point)
        else:
            intersections.add(point)
print(len(intersections))
        

