import pandas as pd
df=pd.read_table("Day2.txt",delimiter=" ")
#Part1
"""depth,hori=0,0
for i in range(len(df)):
    if df["Direction"].iloc[i]=="forward":
        hori+=df["Power"].iloc[i]
    elif df["Direction"].iloc[i]=="up":
        depth-=df["Power"].iloc[i]
    else:
        depth+=df["Power"].iloc[i]
print(depth*hori)"""
depth,hori,aim=0,0,0
for i in range(len(df)):
    if df["Direction"].iloc[i]=="forward":
        hori+=df["Power"].iloc[i]
        depth+=df["Power"].iloc[i]*aim
    elif df["Direction"].iloc[i]=="up":
        aim-=df["Power"].iloc[i]
    else:
        aim+=df["Power"].iloc[i]
print(depth*hori)