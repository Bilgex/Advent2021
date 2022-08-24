import pandas as pd
import numpy as np
drawn_numbers=[76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98
]
df=pd.read_table("Day4.txt",header=None,delim_whitespace=True)
bingo_boards=np.array(df,dtype=object)


def checker(board):
    for i in range(5):
        count_r=0
        count_c=0
        for j in range(5):
            if board[i,j]=="X":
                count_r+=1
            
            if board[j,i]=="X":
                count_c+=1
        if count_r==5 or count_c==5:
            return "WIN"
def unmarksum(board):
    sum=0
    for i in range(5):
        for j in range(5):
            try: 
                sum+=board[i][j]
            except:
                pass
    return sum

def play():
    for drawn in drawn_numbers:
        bingo_boards[bingo_boards==drawn]="X"
        for i in range(0,500,5):
            
            if checker(bingo_boards[i:i+5,0:])=="WIN":
                return unmarksum((bingo_boards[i:i+5,0:]))*drawn
#print(play())
#Part2
def lose():
    winner=[]
    aday=list(range(100))
    for drawn in drawn_numbers:
        bingo_boards[bingo_boards==drawn]="X"
        aday_new=[]
        for i in [a*5 for a in aday]:
                       
            if checker(bingo_boards[i:i+5,0:])=="WIN":
                winner.append((i/5,unmarksum((bingo_boards[i:i+5,0:]))*drawn))
            else:
                aday_new.append(int(i/5))
        aday=aday_new
    return winner
print(lose())
