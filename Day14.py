from collections import defaultdict
from typing import Counter
from copy import deepcopy

with open("Day14.txt") as f:
    lines=f.readlines()
    
path_pieces=[l.replace("\n","").split("->") for l in lines]
n_step_dict={}
base_polymer=path_pieces[0][0]
for poly in  path_pieces[2:]:
    if poly[0][0]==poly[0][1] and poly[0][0]==poly[1][1]:
            n_step_dict[poly[0][0]+poly[0][1]]={1:{poly[0][0]+poly[1][1]:2}}
    else:
            n_step_dict[poly[0][0]+poly[0][1]]={1:{poly[0][0]+poly[1][1]:1,poly[1][1]+poly[0][1]:1}}

#Fail
"""
def transform(polymer:str,position=0):
    next_polymer=""
    if len(polymer)>2:
        if position !=len(polymer)-2:
            if position==0:
                next_polymer+=polymer[position]+poly_trans[polymer[position]+polymer[position+1]]+polymer[position+1]+transform(polymer,position+1)
            else:
                next_polymer+=poly_trans[polymer[position]+polymer[position+1]]+polymer[position+1]+transform(polymer,position+1)
        else:
            return poly_trans[polymer[position]+polymer[position+1]]+polymer[position+1]
    else:
        return polymer[position]+poly_trans[polymer[position]+polymer[position+1]]+polymer[position+1]
    return next_polymer
def mitosis(step,piece):
    piece
    for i in range(step):
        piece=transform(piece)
    return piece
counter_list=[]
for i in range(len(base_polymer)-1):
    if i!=len(base_polymer)-2:
        stepped_piece=mitosis(10,base_polymer[i]+base_polymer[i+1])
        stepped_piece=stepped_piece[:len(stepped_piece)-1]
        counter_list.append(Counter(stepped_piece))

    else:
        stepped_piece=mitosis(10,base_polymer[i]+base_polymer[i+1])
        counter_list.append(Counter(stepped_piece))
        

def def_value():
    return 0
sum_dict=defaultdict(def_value)
for c_dict in counter_list:
    for key,value in c_dict.items():
        sum_dict[key]+=value
print({k:v for k,v in sorted(sum_dict.items(),key=lambda item:item[1])})
"""
def def_value():
    return 0
sum_dict=defaultdict(def_value)   
#Part1
"""
def generate(base_polymer,step):
    if step>0:
        for x in range(len(base_polymer)-1):
            generate(base_polymer[x]+poly_trans[base_polymer[x:x+2]],step-1)
            generate(poly_trans[base_polymer[x:x+2]]+base_polymer[x+1],step-1)   
    else:
        sum_dict[base_polymer[0]]+=1

        
generate(base_polymer,10)
sum_dict[base_polymer[-1]]+=1
#print(max(sum_dict.values())-min(sum_dict.values()))
print(sum_dict)

"""
"""
def generate(base_polymer,step):
    if step>0:
        for x in range(len(base_polymer)-1):
            generate(base_polymer[x]+poly_trans[base_polymer[x:x+2]],step-1)
            generate(poly_trans[base_polymer[x:x+2]]+base_polymer[x+1],step-1)   
    else:
        sum_dict[base_polymer]+=1
one_step_dict=poly_trans.copy()
for key in one_step_dict.keys():
    generate(key,1)
    one_step_dict[key]=deepcopy(sum_dict)
    sum_dict.clear()
n_step_dict={}"""
def climber(double_poly,target):
    max_key=max(n_step_dict[double_poly].keys())
    if target==max_key or target==1 or target in n_step_dict[double_poly].keys():
        return n_step_dict[double_poly][target]
    elif target>max_key*2:
        base_dict=defaultdict(def_value)
        for key in n_step_dict[double_poly][max_key].keys():
            for subkey in climber(key,max_key).keys():
                base_dict[subkey]+=n_step_dict[double_poly][max_key][key]*climber(key,max_key)[subkey]
        n_step_dict[double_poly].update({max_key*2:base_dict})
        return climber(double_poly,target)
    else:
        base_dict=defaultdict(def_value)
        for key in n_step_dict[double_poly][max_key].keys():
            for subkey in climber(key,target-max_key).keys():
                base_dict[subkey]+=n_step_dict[double_poly][max_key][key]*climber(key,target-max_key)[subkey]
        n_step_dict[double_poly].update({target:base_dict})
        return climber(double_poly,target)

 
listem=[]
for key in n_step_dict.keys():
    for subkey in n_step_dict[key][1].keys():
        listem.append(subkey)
stupid_priority=Counter(listem).most_common()

priority_group_A=[]
priority_group_B=[]
for key,_ in stupid_priority:
    if key in n_step_dict[key][1].keys():
        priority_group_A.append(key)
    else:
        priority_group_B.append(key)
priority_key_list=priority_group_A+priority_group_B+list(set(n_step_dict.keys()).difference(set(listem)))
def stepper(step):
    for key in priority_key_list:
        climber(key,step)
   
for x in range(1,4):
    stepper(2**x)
for x in range(2,5):
    stepper(8*x)
dict_list=[]

for x in range(len(base_polymer)-1):
    dict_list.append(climber(base_polymer[x:x+2],40))

char_dict=defaultdict(def_value)
for key in priority_key_list:
    for dicti in dict_list:
        if key in dicti.keys():
            char_dict[key[0]]+=dicti[key]
            char_dict[key[1]]+=dicti[key]
char_dict[base_polymer[0]]+=1
char_dict[base_polymer[-1]]+=1
print((max(char_dict.values())-min(char_dict.values()))//2)